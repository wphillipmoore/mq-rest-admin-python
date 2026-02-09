"""Idempotent ensure methods for MQ object management."""

from __future__ import annotations

import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence


class EnsureResult(enum.Enum):
    """Result of an ensure operation.

    Attributes:
        CREATED: The object did not exist and was defined.
        UPDATED: The object existed but attributes differed and were altered.
        UNCHANGED: The object existed and all specified attributes already matched.

    """

    CREATED = "created"
    UPDATED = "updated"
    UNCHANGED = "unchanged"


class MQRESTEnsureMixin:
    """Mixin providing idempotent ensure methods for MQ objects.

    Each ``ensure_*`` method implements a declarative upsert pattern:
    DEFINE when the object does not exist, ALTER only when specified
    attributes differ, and no-op when they already match — preserving
    ``ALTDATE``/``ALTTIME`` for unchanged objects.
    """

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

    def _ensure_object(
        self,
        *,
        name: str,
        request_parameters: Mapping[str, object] | None,
        display_qualifier: str,
        define_qualifier: str,
        alter_qualifier: str,
    ) -> EnsureResult:
        """Core ensure logic shared by all ``ensure_*`` methods.

        Args:
            name: MQ object name.
            request_parameters: Desired attributes to assert/set.
            display_qualifier: MQSC qualifier for the DISPLAY command.
            define_qualifier: MQSC qualifier for the DEFINE command.
            alter_qualifier: MQSC qualifier for the ALTER command.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        current_objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier=display_qualifier,
            name=name,
            request_parameters=None,
            response_parameters=["all"],
        )

        params = dict(request_parameters) if request_parameters else {}

        if not current_objects:
            self._mqsc_command(
                command="DEFINE",
                mqsc_qualifier=define_qualifier,
                name=name,
                request_parameters=params or None,
                response_parameters=None,
            )
            return EnsureResult.CREATED

        if not params:
            return EnsureResult.UNCHANGED

        current = current_objects[0]
        changed: dict[str, object] = {}
        for key, desired_value in params.items():
            current_value = current.get(key)
            if not _values_match(desired_value, current_value):
                changed[key] = desired_value

        if not changed:
            return EnsureResult.UNCHANGED

        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier=alter_qualifier,
            name=name,
            request_parameters=changed,
            response_parameters=None,
        )
        return EnsureResult.UPDATED

    def ensure_qmgr(
        self,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure the queue manager has the specified attributes.

        Unlike other ensure methods, the queue manager always exists and
        cannot be defined or deleted.  This method compares the requested
        attributes against the current state and issues ``ALTER QMGR``
        only when values differ.  Returns ``UPDATED`` or ``UNCHANGED``
        (never ``CREATED``).

        Args:
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        params = dict(request_parameters) if request_parameters else {}
        if not params:
            return EnsureResult.UNCHANGED

        current_objects = self._mqsc_command(
            command="DISPLAY",
            mqsc_qualifier="QMGR",
            name=None,
            request_parameters=None,
            response_parameters=["all"],
        )

        current = current_objects[0] if current_objects else {}
        changed: dict[str, object] = {}
        for key, desired_value in params.items():
            current_value = current.get(key)
            if not _values_match(desired_value, current_value):
                changed[key] = desired_value

        if not changed:
            return EnsureResult.UNCHANGED

        self._mqsc_command(
            command="ALTER",
            mqsc_qualifier="QMGR",
            name=None,
            request_parameters=changed,
            response_parameters=None,
        )
        return EnsureResult.UPDATED

    def ensure_qlocal(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a local queue exists with the specified attributes.

        Args:
            name: Queue name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="QUEUE",
            define_qualifier="QLOCAL",
            alter_qualifier="QLOCAL",
        )

    def ensure_qremote(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a remote queue exists with the specified attributes.

        Args:
            name: Queue name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="QUEUE",
            define_qualifier="QREMOTE",
            alter_qualifier="QREMOTE",
        )

    def ensure_qalias(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure an alias queue exists with the specified attributes.

        Args:
            name: Queue name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="QUEUE",
            define_qualifier="QALIAS",
            alter_qualifier="QALIAS",
        )

    def ensure_qmodel(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a model queue exists with the specified attributes.

        Args:
            name: Queue name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="QUEUE",
            define_qualifier="QMODEL",
            alter_qualifier="QMODEL",
        )

    def ensure_channel(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a channel exists with the specified attributes.

        Args:
            name: Channel name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="CHANNEL",
            define_qualifier="CHANNEL",
            alter_qualifier="CHANNEL",
        )

    def ensure_authinfo(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure an authentication information object exists with the specified attributes.

        Args:
            name: Authentication information object name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="AUTHINFO",
            define_qualifier="AUTHINFO",
            alter_qualifier="AUTHINFO",
        )

    def ensure_listener(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a listener exists with the specified attributes.

        Args:
            name: Listener name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="LISTENER",
            define_qualifier="LISTENER",
            alter_qualifier="LISTENER",
        )

    def ensure_namelist(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a namelist exists with the specified attributes.

        Args:
            name: Namelist name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="NAMELIST",
            define_qualifier="NAMELIST",
            alter_qualifier="NAMELIST",
        )

    def ensure_process(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a process exists with the specified attributes.

        Args:
            name: Process name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="PROCESS",
            define_qualifier="PROCESS",
            alter_qualifier="PROCESS",
        )

    def ensure_service(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a service exists with the specified attributes.

        Args:
            name: Service name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="SERVICE",
            define_qualifier="SERVICE",
            alter_qualifier="SERVICE",
        )

    def ensure_topic(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a topic exists with the specified attributes.

        Args:
            name: Topic name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="TOPIC",
            define_qualifier="TOPIC",
            alter_qualifier="TOPIC",
        )

    def ensure_sub(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a subscription exists with the specified attributes.

        Args:
            name: Subscription name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="SUB",
            define_qualifier="SUB",
            alter_qualifier="SUB",
        )

    def ensure_stgclass(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a storage class exists with the specified attributes.

        Args:
            name: Storage class name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="STGCLASS",
            define_qualifier="STGCLASS",
            alter_qualifier="STGCLASS",
        )

    def ensure_comminfo(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a communication information object exists with the specified attributes.

        Args:
            name: Communication information object name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="COMMINFO",
            define_qualifier="COMMINFO",
            alter_qualifier="COMMINFO",
        )

    def ensure_cfstruct(
        self,
        name: str,
        request_parameters: Mapping[str, object] | None = None,
    ) -> EnsureResult:
        """Ensure a CF structure exists with the specified attributes.

        Args:
            name: CF structure name.
            request_parameters: Desired attributes to assert/set.

        Returns:
            The :class:`EnsureResult` indicating what action was taken.

        """
        return self._ensure_object(
            name=name,
            request_parameters=request_parameters,
            display_qualifier="CFSTRUCT",
            define_qualifier="CFSTRUCT",
            alter_qualifier="CFSTRUCT",
        )


def _values_match(desired: object, current: object) -> bool:
    """Compare desired and current attribute values.

    Normalizes both sides to strings for comparison, since the MQ REST
    API returns string values but callers may pass int or str.
    Case-insensitive string comparison is used because MQ attribute
    values are case-insensitive.
    """
    if current is None:
        return False
    return str(desired).strip().upper() == str(current).strip().upper()
