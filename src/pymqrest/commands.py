"""MQSC command methods for MQRESTSession."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence


class MQRESTCommandMixin:
    """Mixin providing MQSC command wrapper methods.

    This class is mixed into :class:`~pymqrest.session.MQRESTSession` to
    provide one Python method per MQSC command.  Each method delegates to
    :meth:`_mqsc_command`, which is implemented by the session class.

    See `MQSC reference
    <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
    for the full IBM MQ 9.4 command reference.
    """

    def _mqsc_command(
        self,
        *,
        command: str,
        mqsc_qualifier: str,
        name: str | None,
        request_parameters: Mapping[str, object] | None,
        response_parameters: Sequence[str] | None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        """Dispatch an MQSC command via the ``runCommandJSON`` REST endpoint.

        Subclasses must override this method.  It is not called directly by
        user code.
        """
        raise NotImplementedError  # pragma: no cover

    # BEGIN GENERATED MQSC METHODS
    def alter_authinfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``ALTER AUTHINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER BUFFPOOL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER CFSTRUCT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER COMMINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER LISTENER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER NAMELIST`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER PROCESS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER PSID`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="PSID",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_qalias(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``ALTER QALIAS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QALIAS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_qlocal(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``ALTER QLOCAL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QLOCAL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_qmgr(
        self,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``ALTER QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QMGR",
            name=None,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_qmodel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``ALTER QMODEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QMODEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def alter_qremote(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``ALTER QREMOTE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QREMOTE",
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
        """Execute the MQSC ``ALTER SECURITY`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER SERVICE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER SMDS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER STGCLASS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER SUB`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER TOPIC`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ALTER TRACE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``ARCHIVE LOG`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``BACKUP CFSTRUCT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``CLEAR QLOCAL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``CLEAR TOPICSTR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE AUTHINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE BUFFPOOL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE CFSTRUCT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="CFSTRUCT",
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
        """Execute the MQSC ``DEFINE CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="CHANNEL",
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
        """Execute the MQSC ``DEFINE COMMINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE LISTENER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE LOG`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE MAXSMSGS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE NAMELIST`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE PROCESS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE PSID`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="PSID",
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
        """Execute the MQSC ``DEFINE QALIAS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QALIAS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def define_qlocal(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``DEFINE QLOCAL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QLOCAL",
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
        """Execute the MQSC ``DEFINE QMODEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QMODEL",
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
        """Execute the MQSC ``DEFINE QREMOTE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DEFINE",
            mqsc_qualifier="QREMOTE",
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
        """Execute the MQSC ``DEFINE SERVICE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE STGCLASS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE SUB`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DEFINE TOPIC`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE AUTHINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE AUTHREC`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE BUFFPOOL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE CFSTRUCT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="CFSTRUCT",
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
        """Execute the MQSC ``DELETE CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="CHANNEL",
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
        """Execute the MQSC ``DELETE COMMINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE LISTENER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE NAMELIST`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE POLICY`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE PROCESS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE PSID`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="PSID",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_qalias(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``DELETE QALIAS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="QALIAS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_qlocal(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``DELETE QLOCAL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="QLOCAL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_qmodel(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``DELETE QMODEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="QMODEL",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    def delete_qremote(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> None:
        """Execute the MQSC ``DELETE QREMOTE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="QREMOTE",
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
        """Execute the MQSC ``DELETE QUEUE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="DELETE",
            mqsc_qualifier="QUEUE",
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
        """Execute the MQSC ``DELETE SERVICE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE STGCLASS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE SUB`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DELETE TOPIC`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``DISPLAY APSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY ARCHIVE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY AUTHINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY AUTHREC`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY AUTHSERV`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY CFSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY CFSTRUCT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CFSTRUCT",
            name=name,
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
        """Execute the MQSC ``DISPLAY CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CHANNEL",
            name=name or "*",
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
        """Execute the MQSC ``DISPLAY CHINIT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY CHLAUTH`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY CHSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY CLUSQMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="CLUSQMGR",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_cmdserv(
        self,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        """Execute the MQSC ``DISPLAY CMDSERV`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Returns:
            Parameter dict, or ``None``.

        """
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

    def display_comminfo(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        """Execute the MQSC ``DISPLAY COMMINFO`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY CONN`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY ENTAUTH`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY GROUP`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY LISTENER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY LOG`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY LSSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY MAXSMSGS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY NAMELIST`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY POLICY`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY PROCESS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY PUBSUB`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="PUBSUB",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_qmgr(
        self,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
    ) -> dict[str, object] | None:
        """Execute the MQSC ``DISPLAY QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Returns:
            Parameter dict, or ``None``.

        """
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
        """Execute the MQSC ``DISPLAY QMSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Returns:
            Parameter dict, or ``None``.

        """
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

    def display_qstatus(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        """Execute the MQSC ``DISPLAY QSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QSTATUS",
            name=name,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
            where=where,
        )

    def display_queue(
        self,
        name: str | None = None,
        request_parameters: Mapping[str, object] | None = None,
        response_parameters: Sequence[str] | None = None,
        where: str | None = None,
    ) -> list[dict[str, object]]:
        """Execute the MQSC ``DISPLAY QUEUE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
        return self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QUEUE",
            name=name or "*",
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
        """Execute the MQSC ``DISPLAY SBSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY SECURITY`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY SERVICE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY SMDS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY SMDSCONN`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY STGCLASS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY SUB`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY SVSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY SYSTEM`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY TCLUSTER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY THREAD`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY TOPIC`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY TPSTATUS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY TRACE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``DISPLAY USAGE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name or generic pattern.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.
            where: Filter expression (e.g. ``"current_depth GT 100"``).
                The keyword is mapped from ``snake_case`` when mapping
                is enabled.

        Returns:
            List of parameter dicts, one per matching object. Empty
            list if no objects match.

        """
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
        """Execute the MQSC ``MOVE QLOCAL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``PING CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``PING QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``PURGE CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RECOVER BSDS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RECOVER CFSTRUCT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``REFRESH CLUSTER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``REFRESH QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``REFRESH SECURITY`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESET CFSTRUCT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESET CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESET CLUSTER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESET QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESET QSTATS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESET SMDS`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESET TPIPE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESOLVE CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESOLVE INDOUBT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RESUME QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``RVERIFY SECURITY`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``SET ARCHIVE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``SET AUTHREC`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``SET CHLAUTH`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``SET LOG`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``SET POLICY`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``SET SYSTEM`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START CHINIT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START CMDSERV`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START LISTENER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START SERVICE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START SMDSCONN`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``START TRACE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP CHANNEL`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP CHINIT`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP CMDSERV`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP CONN`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP LISTENER`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP SERVICE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP SMDSCONN`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``STOP TRACE`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            name: Object name.
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
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
        """Execute the MQSC ``SUSPEND QMGR`` command.

        See `MQSC reference <https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands>`__
        for command details.

        Args:
            request_parameters: Request attributes as a dict. Mapped
                from ``snake_case`` when mapping is enabled.
            response_parameters: Response attributes to return.
                Defaults to ``["all"]``.

        Raises:
            MQRESTCommandError: If the command fails.

        """
        self._mqsc_command(
            command="SUSPEND",
            mqsc_qualifier="QMGR",
            name=None,
            request_parameters=request_parameters,
            response_parameters=response_parameters,
        )

    # END GENERATED MQSC METHODS
