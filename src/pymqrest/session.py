"""MQ REST API session and command execution."""

from __future__ import annotations

import base64
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Protocol, cast

import requests
from requests import RequestException

from .auth import LTPA_COOKIE_NAME, BasicAuth, CertificateAuth, Credentials, LTPAAuth, perform_ltpa_login
from .commands import MQRESTCommandMixin
from .ensure import MQRESTEnsureMixin
from .exceptions import (
    MQRESTCommandError,
    MQRESTResponseError,
    MQRESTTransportError,
)
from .mapping import MappingError, MappingIssue, map_request_attributes, map_response_list
from .mapping_data import MAPPING_DATA

DEFAULT_RESPONSE_PARAMETERS: list[str] = ["all"]
DEFAULT_CSRF_TOKEN = "local"  # noqa: S105
ERROR_TRANSPORT_FAILURE = "Failed to reach MQ REST endpoint."
ERROR_INVALID_JSON = "Response body was not valid JSON."
ERROR_NON_OBJECT_RESPONSE = "Response payload was not a JSON object."
ERROR_COMMAND_RESPONSE_NOT_LIST = "Response commandResponse was not a list."
ERROR_COMMAND_RESPONSE_ITEM_NOT_OBJECT = "Response commandResponse item was not an object."


@dataclass(frozen=True)
class TransportResponse:
    """Container for the raw HTTP response returned by a transport.

    Attributes:
        status_code: The HTTP status code (e.g. ``200``, ``401``).
        text: The response body as text.
        headers: The response headers as a string-to-string mapping.

    """

    status_code: int
    text: str
    headers: Mapping[str, str]


class MQRESTTransport(Protocol):
    """Protocol for MQ REST transport implementations.

    Implement this protocol to provide a custom HTTP transport
    (e.g. for testing or for an alternative HTTP client library).
    The default implementation is :class:`RequestsTransport`.
    """

    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse:
        """Send a JSON payload via HTTP POST and return the response.

        Args:
            url: The fully-qualified URL to POST to.
            payload: The JSON-serialisable request body.
            headers: HTTP headers to include in the request.
            timeout_seconds: Request timeout in seconds, or ``None``
                for no timeout.
            verify_tls: Whether to verify the server's TLS certificate.

        Returns:
            A :class:`TransportResponse` with the status code, body
            text, and response headers.

        Raises:
            MQRESTTransportError: If the request cannot be completed.

        """


class RequestsTransport:
    """Default :class:`MQRESTTransport` implementation using ``requests``.

    Wraps a :class:`requests.Session` to handle JSON POST requests
    to the MQ REST API. Connection-level errors are translated into
    :class:`~pymqrest.exceptions.MQRESTTransportError`.
    """

    def __init__(
        self,
        session: requests.Session | None = None,
        *,
        client_cert: tuple[str, str] | str | None = None,
    ) -> None:
        """Initialize the transport.

        Args:
            session: An existing :class:`requests.Session` to reuse,
                or ``None`` to create a new one.
            client_cert: Client certificate for mutual TLS. Either a
                path to a combined cert/key PEM file, or a
                ``(cert_path, key_path)`` tuple.

        """
        self._session = session or requests.Session()
        if client_cert is not None:
            self._session.cert = client_cert

    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse:
        """Send a JSON payload via HTTP POST and return the response.

        Args:
            url: The fully-qualified URL to POST to.
            payload: The JSON-serialisable request body.
            headers: HTTP headers to include in the request.
            timeout_seconds: Request timeout in seconds, or ``None``
                for no timeout.
            verify_tls: Whether to verify the server's TLS certificate.

        Returns:
            A :class:`TransportResponse` with the status code, body
            text, and response headers.

        Raises:
            MQRESTTransportError: If the underlying ``requests`` call
                raises a :class:`~requests.RequestException`.

        """
        try:
            response = self._session.post(
                url,
                json=dict(payload),
                headers=dict(headers),
                timeout=timeout_seconds,
                verify=verify_tls,
            )
        except RequestException as error:
            raise MQRESTTransportError(ERROR_TRANSPORT_FAILURE, url=url) from error
        return TransportResponse(
            status_code=response.status_code,
            text=response.text,
            headers=dict(response.headers.items()),
        )


class MQRESTSession(MQRESTEnsureMixin, MQRESTCommandMixin):
    """Session wrapper for MQ REST admin calls.

    Provides MQSC command execution via the IBM MQ ``runCommandJSON``
    REST endpoint. Attribute mapping between ``snake_case`` and native
    MQSC parameter names is enabled by default.

    All MQSC command methods are inherited from
    :class:`~pymqrest.commands.MQRESTCommandMixin` — see
    :doc:`/api/commands` for the full list.

    Attributes:
        last_response_payload: The parsed JSON payload from the most
            recent command, or ``None`` before any command is executed.
        last_response_text: The raw HTTP response body from the most
            recent command, or ``None``.
        last_http_status: The HTTP status code from the most recent
            command, or ``None``.
        last_command_payload: The ``runCommandJSON`` request payload
            sent for the most recent command, or ``None``.

    """

    def __init__(  # noqa: PLR0913
        self,
        rest_base_url: str,
        qmgr_name: str,
        *,
        credentials: Credentials,
        verify_tls: bool = True,
        timeout_seconds: float | None = 30.0,
        map_attributes: bool = True,
        mapping_strict: bool = True,
        csrf_token: str | None = DEFAULT_CSRF_TOKEN,
        transport: MQRESTTransport | None = None,
    ) -> None:
        """Initialize an MQ REST session.

        Args:
            rest_base_url: Base URL of the MQ REST API
                (e.g. ``"https://localhost:9443/ibmmq/rest/v2"``).
            qmgr_name: Name of the target queue manager.
            credentials: A credential object (:class:`~pymqrest.auth.BasicAuth`,
                :class:`~pymqrest.auth.LTPAAuth`, or
                :class:`~pymqrest.auth.CertificateAuth`).
            verify_tls: Whether to verify the server's TLS certificate.
                Set to ``False`` for self-signed certificates.
            timeout_seconds: HTTP request timeout in seconds, or
                ``None`` for no timeout.
            map_attributes: When ``True`` (default), translate attribute
                names between ``snake_case`` and MQSC forms
                automatically.
            mapping_strict: When ``True`` (default), raise
                :class:`~pymqrest.mapping.MappingError` on any
                unrecognised attribute. When ``False``, pass
                unrecognised attributes through unchanged.
            csrf_token: CSRF token value for the
                ``ibm-mq-rest-csrf-token`` header. Defaults to
                ``"local"``. Set to ``None`` to omit the header.
            transport: Custom :class:`MQRESTTransport` implementation.
                Defaults to :class:`RequestsTransport`.

        Raises:
            MQRESTAuthError: If LTPA login fails at construction time.

        """
        self._rest_base_url = rest_base_url.rstrip("/")
        self._qmgr_name = qmgr_name
        self._verify_tls = verify_tls
        self._timeout_seconds = timeout_seconds
        self._map_attributes = map_attributes
        self._mapping_strict = mapping_strict
        self._csrf_token = csrf_token
        self._credentials = credentials

        if isinstance(credentials, CertificateAuth) and transport is None:
            cert = (
                (credentials.cert_path, credentials.key_path)
                if credentials.key_path is not None
                else credentials.cert_path
            )
            self._transport: MQRESTTransport = RequestsTransport(client_cert=cert)
        else:
            self._transport = transport or RequestsTransport()

        self._ltpa_token: str | None = None
        if isinstance(credentials, LTPAAuth):
            self._ltpa_token = perform_ltpa_login(
                self._transport,
                self._rest_base_url,
                credentials,
                csrf_token=self._csrf_token,
                timeout_seconds=self._timeout_seconds,
                verify_tls=self._verify_tls,
            )

        self.last_response_payload: dict[str, object] | None = None
        self.last_response_text: str | None = None
        self.last_http_status: int | None = None
        self.last_command_payload: dict[str, object] | None = None

    @property
    def qmgr_name(self) -> str:
        """The queue manager name this session targets."""
        return self._qmgr_name

    def _mqsc_command(  # noqa: PLR0913
        self,
        *,
        command: str,
        mqsc_qualifier: str,
        name: str | None,
        request_parameters: Mapping[str, object] | None,
        response_parameters: Sequence[str] | None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        command_upper = command.strip().upper()
        qualifier_upper = mqsc_qualifier.strip().upper()
        normalized_request_parameters = dict(request_parameters or {})
        normalized_response_parameters = _normalize_response_parameters(
            response_parameters,
            is_display=command_upper == "DISPLAY",
        )
        map_attributes = self._map_attributes
        mapping_qualifier = self._resolve_mapping_qualifier(command_upper, qualifier_upper)

        if map_attributes:
            normalized_request_parameters = map_request_attributes(
                mapping_qualifier,
                normalized_request_parameters,
                strict=self._mapping_strict,
            )
            normalized_response_parameters = self._map_response_parameters(
                command_upper,
                qualifier_upper,
                mapping_qualifier,
                normalized_response_parameters,
            )

        if where is not None and where.strip():
            mapped_where = where
            if map_attributes:
                mapped_where = _map_where_keyword(
                    where,
                    mapping_qualifier,
                    strict=self._mapping_strict,
                )
            normalized_request_parameters["WHERE"] = mapped_where

        payload = _build_command_payload(
            command=command_upper,
            qualifier=qualifier_upper,
            name=name,
            request_parameters=normalized_request_parameters,
            response_parameters=normalized_response_parameters,
        )
        self.last_command_payload = dict(payload)
        transport_response = self._transport.post_json(
            self._build_mqsc_url(),
            payload,
            headers=self._build_headers(),
            timeout_seconds=self._timeout_seconds,
            verify_tls=self._verify_tls,
        )
        self.last_http_status = transport_response.status_code
        self.last_response_text = transport_response.text
        response_payload = _parse_response_payload(transport_response.text)
        self.last_response_payload = response_payload
        _raise_for_command_errors(response_payload, transport_response.status_code)

        command_response = _extract_command_response(response_payload)
        parameter_objects: list[dict[str, object]] = []
        for command_response_item in command_response:
            parameters = command_response_item.get("parameters")
            if isinstance(parameters, Mapping):
                parameters_map = cast("Mapping[str, object]", parameters)
                parameter_objects.append(dict(parameters_map))
            else:
                parameter_objects.append({})

        parameter_objects = _flatten_nested_objects(parameter_objects)

        if map_attributes:
            normalized_objects = [_normalize_response_attributes(item) for item in parameter_objects]
            return map_response_list(
                mapping_qualifier,
                normalized_objects,
                strict=self._mapping_strict,
            )
        return parameter_objects

    def _build_mqsc_url(self) -> str:
        return f"{self._rest_base_url}/admin/action/qmgr/{self._qmgr_name}/mqsc"

    def _build_headers(self) -> dict[str, str]:
        headers: dict[str, str] = {"Accept": "application/json"}
        if isinstance(self._credentials, BasicAuth):
            headers["Authorization"] = _build_basic_auth_header(
                self._credentials.username,
                self._credentials.password,
            )
        elif isinstance(self._credentials, LTPAAuth) and self._ltpa_token is not None:
            headers["Cookie"] = f"{LTPA_COOKIE_NAME}={self._ltpa_token}"
        if self._csrf_token is not None:
            headers["ibm-mq-rest-csrf-token"] = self._csrf_token
        return headers

    def _map_response_parameters(
        self,
        command: str,
        mqsc_qualifier: str,
        mapping_qualifier: str,
        response_parameters: list[str],
    ) -> list[str]:
        if _is_all_response_parameters(response_parameters):
            return response_parameters
        response_parameter_macros = _get_response_parameter_macros(command, mqsc_qualifier)
        macro_lookup = {macro.lower(): macro for macro in response_parameter_macros}
        qualifier_entry = _get_qualifier_entry(mapping_qualifier)
        if qualifier_entry is None:
            if self._mapping_strict:
                raise MappingError(_build_unknown_qualifier_issue(mapping_qualifier))
            return response_parameters
        combined_map = _build_snake_to_mqsc_map(qualifier_entry)
        mapped, issues = _map_response_parameter_names(
            response_parameters,
            macro_lookup,
            combined_map,
            mapping_qualifier,
        )
        if self._mapping_strict and issues:
            raise MappingError(issues)
        return mapped

    def _resolve_mapping_qualifier(self, command: str, mqsc_qualifier: str) -> str:
        command_map = _get_command_map()
        command_key = f"{command} {mqsc_qualifier}"
        command_definition = command_map.get(command_key)
        if isinstance(command_definition, Mapping):
            command_definition_map = cast("Mapping[str, object]", command_definition)
            qualifier = command_definition_map.get("qualifier")
            if isinstance(qualifier, str):
                return qualifier
        fallback = _DEFAULT_MAPPING_QUALIFIERS.get(mqsc_qualifier)
        if fallback is not None:
            return fallback
        return mqsc_qualifier.lower()


def _build_basic_auth_header(username: str, password: str) -> str:
    token = base64.b64encode(f"{username}:{password}".encode()).decode("ascii")
    return f"Basic {token}"


def _build_command_payload(
    *,
    command: str,
    qualifier: str,
    name: str | None,
    request_parameters: Mapping[str, object],
    response_parameters: Sequence[str],
) -> dict[str, object]:
    payload: dict[str, object] = {
        "type": "runCommandJSON",
        "command": command,
        "qualifier": qualifier,
    }
    if name:
        payload["name"] = name
    if request_parameters:
        payload["parameters"] = dict(request_parameters)
    if response_parameters:
        payload["responseParameters"] = list(response_parameters)
    return payload


def _normalize_response_parameters(
    response_parameters: Sequence[str] | None,
    *,
    is_display: bool = True,
) -> list[str]:
    if response_parameters is None:
        return list(DEFAULT_RESPONSE_PARAMETERS) if is_display else []
    normalized_parameters = list(response_parameters)
    if _is_all_response_parameters(normalized_parameters):
        return list(DEFAULT_RESPONSE_PARAMETERS)
    return normalized_parameters


def _is_all_response_parameters(response_parameters: Sequence[str]) -> bool:
    return any(parameter.lower() == "all" for parameter in response_parameters)


def _flatten_nested_objects(
    parameter_objects: list[dict[str, object]],
) -> list[dict[str, object]]:
    flattened: list[dict[str, object]] = []
    for item in parameter_objects:
        objects = item.get("objects")
        if isinstance(objects, list):
            shared = {key: value for key, value in item.items() if key != "objects"}
            for nested_item in objects:
                if isinstance(nested_item, Mapping):
                    merged = dict(shared)
                    merged.update(nested_item)
                    flattened.append(merged)
        else:
            flattened.append(item)
    return flattened


def _normalize_response_attributes(attributes: Mapping[str, object]) -> dict[str, object]:
    normalized: dict[str, object] = {}
    for attribute_name, attribute_value in attributes.items():
        normalized[attribute_name.upper()] = attribute_value
    return normalized


def _parse_response_payload(response_text: str) -> dict[str, object]:
    try:
        decoded = json.loads(response_text)
    except json.JSONDecodeError as error:
        raise MQRESTResponseError(ERROR_INVALID_JSON, response_text=response_text) from error
    if not isinstance(decoded, dict):
        raise MQRESTResponseError(ERROR_NON_OBJECT_RESPONSE, response_text=response_text)
    return decoded


def _extract_command_response(payload: Mapping[str, object]) -> list[dict[str, object]]:
    command_response = payload.get("commandResponse")
    if command_response is None:
        return []
    if not isinstance(command_response, list):
        raise MQRESTResponseError(ERROR_COMMAND_RESPONSE_NOT_LIST)
    response_items: list[dict[str, object]] = []
    for response_item in command_response:
        if not isinstance(response_item, Mapping):
            raise MQRESTResponseError(ERROR_COMMAND_RESPONSE_ITEM_NOT_OBJECT)
        response_item_map = cast("Mapping[str, object]", response_item)
        response_items.append(dict(response_item_map))
    return response_items


def _raise_for_command_errors(payload: Mapping[str, object], status_code: int) -> None:
    overall_completion_code = _extract_optional_int(payload.get("overallCompletionCode"))
    overall_reason_code = _extract_optional_int(payload.get("overallReasonCode"))
    has_overall_error = _has_error_codes(overall_completion_code, overall_reason_code)

    command_response = payload.get("commandResponse")
    command_issues: list[str] = []
    if isinstance(command_response, list):
        for item_index, response_item in enumerate(command_response):
            if not isinstance(response_item, Mapping):
                continue
            response_item_map = cast("Mapping[str, object]", response_item)
            completion_code = _extract_optional_int(response_item_map.get("completionCode"))
            reason_code = _extract_optional_int(response_item_map.get("reasonCode"))
            if _has_error_codes(completion_code, reason_code):
                command_issues.append(
                    " ".join(
                        [
                            f"index={item_index}",
                            f"completionCode={completion_code}",
                            f"reasonCode={reason_code}",
                        ],
                    ),
                )

    if has_overall_error or command_issues:
        message_lines = ["MQ REST command failed."]
        if has_overall_error:
            message_lines.append(
                " ".join(
                    [
                        f"overallCompletionCode={overall_completion_code}",
                        f"overallReasonCode={overall_reason_code}",
                    ],
                ),
            )
        if command_issues:
            message_lines.append("commandResponse:")
            message_lines.extend(command_issues)
        raise MQRESTCommandError(
            "\n".join(message_lines),
            payload=payload,
            status_code=status_code,
        )


def _extract_optional_int(value: object) -> int | None:
    if isinstance(value, int):
        return value
    return None


def _has_error_codes(completion_code: int | None, reason_code: int | None) -> bool:
    return bool(
        (completion_code is not None and completion_code != 0) or (reason_code is not None and reason_code != 0),
    )


def _get_command_map() -> Mapping[str, object]:
    commands = MAPPING_DATA.get("commands")
    if isinstance(commands, Mapping):
        return cast("Mapping[str, object]", commands)
    return {}


def _get_response_parameter_macros(command: str, mqsc_qualifier: str) -> list[str]:
    command_key = f"{command} {mqsc_qualifier}"
    commands = _get_command_map()
    entry = commands.get(command_key)
    if not isinstance(entry, Mapping):
        return []
    entry_map = cast("Mapping[str, object]", entry)
    macros = entry_map.get("response_parameter_macros")
    if not isinstance(macros, Sequence) or isinstance(macros, (str, bytes)):
        return []
    return [macro for macro in macros if isinstance(macro, str)]


def _build_unknown_qualifier_issue(qualifier: str) -> list[MappingIssue]:
    return [
        MappingIssue(
            direction="request",
            reason="unknown_qualifier",
            attribute_name="*",
            qualifier=qualifier,
        ),
    ]


def _build_snake_to_mqsc_map(qualifier_entry: Mapping[str, object]) -> dict[str, str]:
    request_key_map = qualifier_entry.get("request_key_map", {})
    response_key_map = qualifier_entry.get("response_key_map", {})
    response_lookup: dict[str, str] = {}
    if isinstance(response_key_map, Mapping):
        for mqsc_key, snake_key in response_key_map.items():
            if isinstance(mqsc_key, str) and isinstance(snake_key, str):
                response_lookup.setdefault(snake_key, mqsc_key)
    combined_map = dict(response_lookup)
    if isinstance(request_key_map, Mapping):
        combined_map.update({key: value for key, value in request_key_map.items() if isinstance(value, str)})
    return combined_map


def _map_where_keyword(
    where: str,
    mapping_qualifier: str,
    *,
    strict: bool,
) -> str:
    parts = where.strip().split(None, 1)
    keyword = parts[0]
    rest = parts[1] if len(parts) > 1 else ""

    qualifier_entry = _get_qualifier_entry(mapping_qualifier)
    if qualifier_entry is None:
        if strict:
            raise MappingError(_build_unknown_qualifier_issue(mapping_qualifier))
        return where

    combined_map = _build_snake_to_mqsc_map(qualifier_entry)
    mapped_keyword = combined_map.get(keyword)

    if mapped_keyword is None:
        if strict:
            raise MappingError(
                [
                    MappingIssue(
                        direction="request",
                        reason="unknown_key",
                        attribute_name=keyword,
                        qualifier=mapping_qualifier,
                    ),
                ],
            )
        mapped_keyword = keyword

    if rest:
        return f"{mapped_keyword} {rest}"
    return mapped_keyword


def _map_response_parameter_names(
    response_parameters: list[str],
    macro_lookup: Mapping[str, str],
    combined_map: Mapping[str, str],
    mapping_qualifier: str,
) -> tuple[list[str], list[MappingIssue]]:
    mapped: list[str] = []
    issues: list[MappingIssue] = []
    for name in response_parameters:
        macro_key = macro_lookup.get(name.lower())
        if macro_key is not None:
            mapped.append(macro_key)
            continue
        mapped_key = combined_map.get(name)
        if mapped_key is None:
            issues.append(
                MappingIssue(
                    direction="request",
                    reason="unknown_key",
                    attribute_name=name,
                    qualifier=mapping_qualifier,
                ),
            )
            mapped.append(name)
            continue
        mapped.append(mapped_key)
    return mapped, issues


def _get_qualifier_entry(qualifier: str) -> Mapping[str, object] | None:
    qualifiers = MAPPING_DATA.get("qualifiers")
    if not isinstance(qualifiers, Mapping):
        return None
    qualifier_map = cast("Mapping[str, object]", qualifiers)
    qualifier_entry = qualifier_map.get(qualifier)
    if isinstance(qualifier_entry, Mapping):
        return cast("Mapping[str, object]", qualifier_entry)
    return None


_DEFAULT_MAPPING_QUALIFIERS: dict[str, str] = {
    "QUEUE": "queue",
    "QLOCAL": "queue",
    "QREMOTE": "queue",
    "QALIAS": "queue",
    "QMODEL": "queue",
    "CHANNEL": "channel",
    "QMGR": "qmgr",
}
