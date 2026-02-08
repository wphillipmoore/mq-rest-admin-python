"""MQSC command methods for MQRESTSession."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence


class MQRESTCommandMixin:
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
        raise NotImplementedError  # pragma: no cover

    def display_qmgr(
        self,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QMGR",
            name=None,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )
        if objects:
            return objects[0]
        return None

    def display_qmstatus(
        self,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QMSTATUS",
            name=None,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )
        if objects:
            return objects[0]
        return None

    def display_cmdserv(
        self,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CMDSERV",
            name=None,
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
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QUEUE",
            name=name or "*",
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_channel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHANNEL",
            name=name or "*",
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QMGR",
            name=None,
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
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="APSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_archive(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="ARCHIVE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_authinfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="AUTHINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_authrec(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="AUTHREC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_authserv(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="AUTHSERV",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_cfstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CFSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_cfstruct(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CFSTRUCT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_chinit(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHINIT",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_chlauth(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHLAUTH",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_chstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_clusqmgr(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CLUSQMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_comminfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="COMMINFO",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_conn(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CONN",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_entauth(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="ENTAUTH",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_group(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="GROUP",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_listener(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="LISTENER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_log(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="LOG",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_lsstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="LSSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_maxsmsgs(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="MAXSMSGS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_namelist(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="NAMELIST",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_policy(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="POLICY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_process(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="PROCESS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_pubsub(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="PUBSUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_qstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_sbstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SBSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_security(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SECURITY",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_service(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SERVICE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_smds(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SMDS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_smdsconn(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SMDSCONN",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_stgclass(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="STGCLASS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_sub(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_svstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SVSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_system(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="SYSTEM",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_tcluster(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TCLUSTER",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_thread(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="THREAD",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_topic(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TOPIC",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_tpstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TPSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_trace(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="TRACE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_usage(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="USAGE",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="PING",
            mqsc_qualifier="QMGR",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="REFRESH",
            mqsc_qualifier="QMGR",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESET",
            mqsc_qualifier="QMGR",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="RESUME",
            mqsc_qualifier="QMGR",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="CMDSERV",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="START",
            mqsc_qualifier="QMGR",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="CMDSERV",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier="QMGR",
            name=None,
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
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        self._mqsc_command(
            command="SUSPEND",
            mqsc_qualifier="QMGR",
            name=None,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    # END GENERATED MQSC METHODS
