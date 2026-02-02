"""MQ REST API session and command execution."""

from __future__ import annotations

import base64
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Protocol, cast

import requests
from requests import RequestException

from .exceptions import (
    MQRESTCommandError,
    MQRESTResponseError,
    MQRESTTransportError,
)
from .mapping import map_request_attributes, map_response_list
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


class MQRESTSession:
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

    def display_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )
        if objects:
            return objects[0]
        return None

    def display_qmstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QMSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )
        if objects:
            return objects[0]
        return None

    def display_cmdserv(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CMDSERV",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )
        if objects:
            return objects[0]
        return None

    def display_queue(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QUEUE",
            name=name or "*",
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHANNEL",
            name=name or "*",
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_qlocal(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QLOCAL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_qremote(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QREMOTE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_qalias(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QALIAS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_qmodel(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QMODEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_queue(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="QUEUE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_channel(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_channel(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    # BEGIN GENERATED MQSC METHODS
    def alter_authinfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="AUTHINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_buffpool(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="BUFFPOOL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_comminfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="COMMINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_listener(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="LISTENER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_namelist(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="NAMELIST",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_process(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="PROCESS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_psid(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="PSID",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_security(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="SECURITY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_service(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="SERVICE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_smds(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="SMDS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_stgclass(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="STGCLASS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_sub(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="SUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_topic(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="TOPIC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_trace(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="TRACE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def archive_log(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ARCHIVE",
            mqsc_qualifier="LOG",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def backup_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="BACKUP",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def clear_qlocal(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="CLEAR",
            mqsc_qualifier="QLOCAL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def clear_topicstr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="CLEAR",
            mqsc_qualifier="TOPICSTR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_authinfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="AUTHINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_buffpool(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="BUFFPOOL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_comminfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="COMMINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_listener(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="LISTENER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_log(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="LOG",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_maxsmsgs(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="MAXSMSGS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_namelist(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="NAMELIST",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_process(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="PROCESS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_psid(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="PSID",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_service(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="SERVICE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_stgclass(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="STGCLASS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_sub(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="SUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_topic(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="TOPIC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_authinfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="AUTHINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_authrec(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="AUTHREC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_buffpool(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="BUFFPOOL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_comminfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="COMMINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_listener(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="LISTENER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_namelist(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="NAMELIST",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_policy(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="POLICY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_process(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="PROCESS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_psid(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="PSID",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_service(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="SERVICE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_stgclass(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="STGCLASS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_sub(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="SUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_topic(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="TOPIC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_apstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="APSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_archive(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="ARCHIVE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_authinfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="AUTHINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_authrec(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="AUTHREC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_authserv(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="AUTHSERV",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_cfstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CFSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_chinit(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHINIT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_chlauth(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHLAUTH",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_chstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_clusqmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CLUSQMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_comminfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="COMMINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_conn(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CONN",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_entauth(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="ENTAUTH",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_group(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="GROUP",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_listener(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="LISTENER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_log(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="LOG",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_lsstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="LSSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_maxsmsgs(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="MAXSMSGS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_namelist(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="NAMELIST",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_policy(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="POLICY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_process(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="PROCESS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_pubsub(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="PUBSUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_qstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_sbstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SBSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_security(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SECURITY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_service(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SERVICE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_smds(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SMDS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_smdsconn(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SMDSCONN",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_stgclass(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="STGCLASS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_sub(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_svstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SVSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_system(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SYSTEM",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_tcluster(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TCLUSTER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_thread(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="THREAD",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_topic(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TOPIC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_tpstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TPSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_trace(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TRACE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def display_usage(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="USAGE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def move_qlocal(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="MOVE",
            mqsc_qualifier="QLOCAL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def ping_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="PING",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def ping_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="PING",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def purge_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="PURGE",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def recover_bsds(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RECOVER",
            mqsc_qualifier="BSDS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def recover_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RECOVER",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def refresh_cluster(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="REFRESH",
            mqsc_qualifier="CLUSTER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def refresh_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="REFRESH",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def refresh_security(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="REFRESH",
            mqsc_qualifier="SECURITY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def reset_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def reset_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def reset_cluster(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="CLUSTER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def reset_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def reset_qstats(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="QSTATS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def reset_smds(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="SMDS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def reset_tpipe(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="TPIPE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def resolve_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESOLVE",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def resolve_indoubt(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESOLVE",
            mqsc_qualifier="INDOUBT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def resume_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESUME",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def rverify_security(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RVERIFY",
            mqsc_qualifier="SECURITY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def set_archive(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SET",
            mqsc_qualifier="ARCHIVE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def set_authrec(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SET",
            mqsc_qualifier="AUTHREC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def set_chlauth(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SET",
            mqsc_qualifier="CHLAUTH",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def set_log(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SET",
            mqsc_qualifier="LOG",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def set_policy(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SET",
            mqsc_qualifier="POLICY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def set_system(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SET",
            mqsc_qualifier="SYSTEM",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_chinit(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="CHINIT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_cmdserv(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="CMDSERV",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_listener(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="LISTENER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_service(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="SERVICE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_smdsconn(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="SMDSCONN",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def start_trace(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="TRACE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="CHANNEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_chinit(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="CHINIT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_cmdserv(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="CMDSERV",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_conn(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="CONN",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_listener(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="LISTENER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_service(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="SERVICE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_smdsconn(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="SMDSCONN",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def stop_trace(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="TRACE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def suspend_qmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SUSPEND",
            mqsc_qualifier="QMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )
    # END GENERATED MQSC METHODS

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
        mapping_qualifier: str,
        response_parameters: list[str],
    ) -> list[str]:
        if _is_all_response_parameters(response_parameters):
            return response_parameters
        mapping_input = dict.fromkeys(response_parameters, None)
        mapped = map_request_attributes(
            mapping_qualifier,
            mapping_input,
            strict=self._mapping_strict,
        )
        return list(mapped.keys())

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


_DEFAULT_MAPPING_QUALIFIERS: dict[str, str] = {
    "QUEUE": "queue",
    "QLOCAL": "queue",
    "QREMOTE": "queue",
    "QALIAS": "queue",
    "QMODEL": "queue",
    "CHANNEL": "channel",
    "QMGR": "qmgr",
}
