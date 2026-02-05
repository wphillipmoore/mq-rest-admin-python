"""MQ REST API session and command execution."""

from __future__ import annotations

import base64
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Protocol, cast

import requests
from requests import RequestException

from .commands import MQRESTCommandMixin
from .exceptions import (
    MQRESTCommandError,
    MQRESTResponseError,
    MQRESTTransportError,
)
from .mapping import MappingError, MappingIssue, map_request_attributes, map_response_list
from .mapping_data import MAPPING_DATA

DEFAULT_RESPONSE_PARAMETERS: list[str] = ["all"]


@dataclass(frozen=True)
class TransportResponse:
    status_code: int
    text: str
    headers: Mapping[str, str]


class MQRESTTransport(Protocol):
    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse:
        """Send JSON payload to URL and return the raw response."""


class RequestsTransport:
    """Requests-based transport for MQ REST requests."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self._session = session or requests.Session()

    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse:
        try:
            response = self._session.post(
                url,
                json=dict(payload),
                headers=dict(headers),
                timeout=timeout_seconds,
                verify=verify_tls,
            )
        except RequestException as error:
            raise MQRESTTransportError("Failed to reach MQ REST endpoint.", url=url) from error
        return TransportResponse(
            status_code=response.status_code,
            text=response.text,
            headers=dict(response.headers.items()),
        )


class MQRESTSession(MQRESTCommandMixin):
    """Session wrapper for MQ REST admin calls."""

    def __init__(
        self,
        rest_base_url: str,
        qmgr_name: str,
        username: str,
        password: str,
        *,
        verify_tls: bool = True,
        timeout_seconds: float | None = 30.0,
        map_attributes: bool = True,
        mapping_strict: bool = False,
        csrf_token: str | None = "local",
        transport: MQRESTTransport | None = None,
    ) -> None:
        self._rest_base_url = rest_base_url.rstrip("/")
        self._qmgr_name = qmgr_name
        self._verify_tls = verify_tls
        self._timeout_seconds = timeout_seconds
        self._map_attributes = map_attributes
        self._mapping_strict = mapping_strict
        self._csrf_token = csrf_token
        self._transport = transport or RequestsTransport()
        self._authorization_header = _build_basic_auth_header(username, password)

        self.last_response_payload: dict[str, object] | None = None
        self.last_response_text: str | None = None
        self.last_http_status: int | None = None
        self.last_command_payload: dict[str, object] | None = None

    def _mqsc_command(
        self,
        *,
        command: str,
        mqsc_qualifier: str,
        name: str | None,
        request_parameters: Mapping[str, object] | None,
        response_parameters: Sequence[str] | None,
    ) -> list[dict[str, object]]:
        command_upper = command.strip().upper()
        qualifier_upper = mqsc_qualifier.strip().upper()
        normalized_request_parameters = dict(request_parameters or {})
        normalized_response_parameters = _normalize_response_parameters(response_parameters)
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
        headers = {
            "Authorization": self._authorization_header,
            "Accept": "application/json",
        }
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
                raise MappingError(
                    [
                        MappingIssue(
                            direction="request",
                            reason="unknown_qualifier",
                            attribute_name="*",
                            qualifier=mapping_qualifier,
                        )
                    ]
                )
            return response_parameters

        request_key_map = qualifier_entry.get("request_key_map", {})
        response_key_map = qualifier_entry.get("response_key_map", {})
        response_lookup: dict[str, str] = {}
        if isinstance(response_key_map, Mapping):
            for mqsc_key, snake_key in response_key_map.items():
                if isinstance(mqsc_key, str) and isinstance(snake_key, str):
                    response_lookup.setdefault(snake_key, mqsc_key)
        combined_map = dict(response_lookup)
        if isinstance(request_key_map, Mapping):
            combined_map.update({k: v for k, v in request_key_map.items() if isinstance(v, str)})

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
                    )
                )
                mapped.append(name)
            else:
                mapped.append(mapped_key)
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


def _normalize_response_parameters(response_parameters: Sequence[str] | None) -> list[str]:
    if response_parameters is None:
        return list(DEFAULT_RESPONSE_PARAMETERS)
    normalized_parameters = list(response_parameters)
    if _is_all_response_parameters(normalized_parameters):
        return list(DEFAULT_RESPONSE_PARAMETERS)
    return normalized_parameters


def _is_all_response_parameters(response_parameters: Sequence[str]) -> bool:
    return any(parameter.lower() == "all" for parameter in response_parameters)


def _normalize_response_attributes(attributes: Mapping[str, object]) -> dict[str, object]:
    normalized: dict[str, object] = {}
    for attribute_name, attribute_value in attributes.items():
        normalized[attribute_name.upper()] = attribute_value
    return normalized


def _parse_response_payload(response_text: str) -> dict[str, object]:
    try:
        decoded = json.loads(response_text)
    except json.JSONDecodeError as error:
        raise MQRESTResponseError("Response body was not valid JSON.", response_text=response_text) from error
    if not isinstance(decoded, dict):
        raise MQRESTResponseError("Response payload was not a JSON object.", response_text=response_text)
    return decoded


def _extract_command_response(payload: Mapping[str, object]) -> list[dict[str, object]]:
    command_response = payload.get("commandResponse")
    if command_response is None:
        return []
    if not isinstance(command_response, list):
        raise MQRESTResponseError("Response commandResponse was not a list.")
    response_items: list[dict[str, object]] = []
    for response_item in command_response:
        if not isinstance(response_item, Mapping):
            raise MQRESTResponseError("Response commandResponse item was not an object.")
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
                        ]
                    )
                )

    if has_overall_error or command_issues:
        message_lines = ["MQ REST command failed."]
        if has_overall_error:
            message_lines.append(
                " ".join(
                    [
                        f"overallCompletionCode={overall_completion_code}",
                        f"overallReasonCode={overall_reason_code}",
                    ]
                )
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
        (completion_code is not None and completion_code != 0)
        or (reason_code is not None and reason_code != 0)
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
    normalized: list[str] = []
    for macro in macros:
        if isinstance(macro, str):
            normalized.append(macro)
    return normalized


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
