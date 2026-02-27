"""Synchronous start/stop/restart wrappers for MQ objects."""

from __future__ import annotations

import enum
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .exceptions import MQRESTTimeoutError

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence


@dataclass(frozen=True)
class SyncConfig:
    """Configuration for synchronous polling operations.

    Attributes:
        timeout_seconds: Maximum wall-clock seconds to wait for the
            object to reach the target state.
        poll_interval_seconds: Seconds to sleep between status polls.

    """

    timeout_seconds: float = 30.0
    poll_interval_seconds: float = 1.0


class SyncOperation(enum.Enum):
    """Operation performed by a synchronous wrapper.

    Attributes:
        STARTED: The object was started and confirmed running.
        STOPPED: The object was stopped and confirmed stopped.
        RESTARTED: The object was stopped then started.

    """

    STARTED = "started"
    STOPPED = "stopped"
    RESTARTED = "restarted"


@dataclass(frozen=True)
class SyncResult:
    """Result of a synchronous start/stop/restart operation.

    Attributes:
        operation: The :class:`SyncOperation` that was performed.
        polls: Total number of status polls issued.
        elapsed_seconds: Total wall-clock seconds from command to
            target state confirmation.

    """

    operation: SyncOperation
    polls: int
    elapsed_seconds: float


@dataclass(frozen=True)
class _ObjectTypeConfig:
    """Per-object-type metadata for polling logic."""

    start_qualifier: str
    stop_qualifier: str
    status_qualifier: str
    status_keys: tuple[str, ...]
    empty_means_stopped: bool


_CHANNEL_CONFIG = _ObjectTypeConfig(
    start_qualifier="CHANNEL",
    stop_qualifier="CHANNEL",
    status_qualifier="CHSTATUS",
    status_keys=("channel_status", "STATUS"),
    empty_means_stopped=True,
)

_LISTENER_CONFIG = _ObjectTypeConfig(
    start_qualifier="LISTENER",
    stop_qualifier="LISTENER",
    status_qualifier="LSSTATUS",
    status_keys=("status", "STATUS"),
    empty_means_stopped=False,
)

_SERVICE_CONFIG = _ObjectTypeConfig(
    start_qualifier="SERVICE",
    stop_qualifier="SERVICE",
    status_qualifier="SVSTATUS",
    status_keys=("status", "STATUS"),
    empty_means_stopped=False,
)

_RUNNING_VALUES = frozenset({"RUNNING", "running"})
_STOPPED_VALUES = frozenset({"STOPPED", "stopped"})


class MQRESTSyncMixin:
    """Mixin providing synchronous start/stop/restart wrappers.

    Each ``*_sync`` method issues the MQSC command then polls the
    corresponding ``DISPLAY *STATUS`` until the object reaches a
    stable state or the timeout expires.  ``restart_*`` methods
    perform a synchronous stop followed by a synchronous start.
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
        raise NotImplementedError  # pragma: no cover

    # ------------------------------------------------------------------
    # Channel
    # ------------------------------------------------------------------

    def start_channel_sync(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Start a channel and wait until it is running.

        Args:
            name: Channel name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with operation details.

        Raises:
            MQRESTTimeoutError: If the channel does not reach RUNNING
                within the timeout.

        """
        return self._start_and_poll(name, _CHANNEL_CONFIG, config)

    def stop_channel_sync(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Stop a channel and wait until it is stopped.

        Args:
            name: Channel name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with operation details.

        Raises:
            MQRESTTimeoutError: If the channel does not reach STOPPED
                within the timeout.

        """
        return self._stop_and_poll(name, _CHANNEL_CONFIG, config)

    def restart_channel(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Stop then start a channel, waiting for each phase.

        Each phase gets the full timeout independently.

        Args:
            name: Channel name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with total polls and elapsed time
            across both phases.

        Raises:
            MQRESTTimeoutError: If either phase exceeds the timeout.

        """
        return self._restart(name, _CHANNEL_CONFIG, config)

    # ------------------------------------------------------------------
    # Listener
    # ------------------------------------------------------------------

    def start_listener_sync(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Start a listener and wait until it is running.

        Args:
            name: Listener name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with operation details.

        Raises:
            MQRESTTimeoutError: If the listener does not reach RUNNING
                within the timeout.

        """
        return self._start_and_poll(name, _LISTENER_CONFIG, config)

    def stop_listener_sync(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Stop a listener and wait until it is stopped.

        Args:
            name: Listener name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with operation details.

        Raises:
            MQRESTTimeoutError: If the listener does not reach STOPPED
                within the timeout.

        """
        return self._stop_and_poll(name, _LISTENER_CONFIG, config)

    def restart_listener(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Stop then start a listener, waiting for each phase.

        Each phase gets the full timeout independently.

        Args:
            name: Listener name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with total polls and elapsed time
            across both phases.

        Raises:
            MQRESTTimeoutError: If either phase exceeds the timeout.

        """
        return self._restart(name, _LISTENER_CONFIG, config)

    # ------------------------------------------------------------------
    # Service
    # ------------------------------------------------------------------

    def start_service_sync(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Start a service and wait until it is running.

        Args:
            name: Service name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with operation details.

        Raises:
            MQRESTTimeoutError: If the service does not reach RUNNING
                within the timeout.

        """
        return self._start_and_poll(name, _SERVICE_CONFIG, config)

    def stop_service_sync(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Stop a service and wait until it is stopped.

        Args:
            name: Service name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with operation details.

        Raises:
            MQRESTTimeoutError: If the service does not reach STOPPED
                within the timeout.

        """
        return self._stop_and_poll(name, _SERVICE_CONFIG, config)

    def restart_service(
        self,
        name: str,
        *,
        config: SyncConfig | None = None,
    ) -> SyncResult:
        """Stop then start a service, waiting for each phase.

        Each phase gets the full timeout independently.

        Args:
            name: Service name.
            config: Optional polling configuration.

        Returns:
            A :class:`SyncResult` with total polls and elapsed time
            across both phases.

        Raises:
            MQRESTTimeoutError: If either phase exceeds the timeout.

        """
        return self._restart(name, _SERVICE_CONFIG, config)

    # ------------------------------------------------------------------
    # Core polling helpers
    # ------------------------------------------------------------------

    def _start_and_poll(
        self,
        name: str,
        obj_config: _ObjectTypeConfig,
        config: SyncConfig | None,
    ) -> SyncResult:
        """Issue START then poll until the object is RUNNING."""
        sync_config = config or SyncConfig()
        self._mqsc_command(
            command="START",
            mqsc_qualifier=obj_config.start_qualifier,
            name=name,
            request_parameters=None,
            response_parameters=None,
        )
        polls = 0
        start_time = time.monotonic()
        while True:
            time.sleep(sync_config.poll_interval_seconds)
            status_rows = self._mqsc_command(
                command="DISPLAY",
                mqsc_qualifier=obj_config.status_qualifier,
                name=name,
                request_parameters=None,
                response_parameters=["all"],
            )
            polls += 1
            if _has_status(status_rows, obj_config.status_keys, _RUNNING_VALUES):
                elapsed = time.monotonic() - start_time
                return SyncResult(SyncOperation.STARTED, polls=polls, elapsed_seconds=elapsed)
            elapsed = time.monotonic() - start_time
            if elapsed >= sync_config.timeout_seconds:
                message = (
                    f"{obj_config.start_qualifier} '{name}' did not reach RUNNING within {sync_config.timeout_seconds}s"
                )
                raise MQRESTTimeoutError(
                    message,
                    name=name,
                    operation="start",
                    elapsed=elapsed,
                )

    def _stop_and_poll(
        self,
        name: str,
        obj_config: _ObjectTypeConfig,
        config: SyncConfig | None,
    ) -> SyncResult:
        """Issue STOP then poll until the object is STOPPED."""
        sync_config = config or SyncConfig()
        self._mqsc_command(
            command="STOP",
            mqsc_qualifier=obj_config.stop_qualifier,
            name=name,
            request_parameters=None,
            response_parameters=None,
        )
        polls = 0
        start_time = time.monotonic()
        while True:
            time.sleep(sync_config.poll_interval_seconds)
            status_rows = self._mqsc_command(
                command="DISPLAY",
                mqsc_qualifier=obj_config.status_qualifier,
                name=name,
                request_parameters=None,
                response_parameters=["all"],
            )
            polls += 1
            if obj_config.empty_means_stopped and not status_rows:
                elapsed = time.monotonic() - start_time
                return SyncResult(SyncOperation.STOPPED, polls=polls, elapsed_seconds=elapsed)
            if _has_status(status_rows, obj_config.status_keys, _STOPPED_VALUES):
                elapsed = time.monotonic() - start_time
                return SyncResult(SyncOperation.STOPPED, polls=polls, elapsed_seconds=elapsed)
            elapsed = time.monotonic() - start_time
            if elapsed >= sync_config.timeout_seconds:
                message = (
                    f"{obj_config.stop_qualifier} '{name}' did not reach STOPPED within {sync_config.timeout_seconds}s"
                )
                raise MQRESTTimeoutError(
                    message,
                    name=name,
                    operation="stop",
                    elapsed=elapsed,
                )

    def _restart(
        self,
        name: str,
        obj_config: _ObjectTypeConfig,
        config: SyncConfig | None,
    ) -> SyncResult:
        """Stop-sync then start-sync, returning combined totals."""
        stop_result = self._stop_and_poll(name, obj_config, config)
        start_result = self._start_and_poll(name, obj_config, config)
        return SyncResult(
            SyncOperation.RESTARTED,
            polls=stop_result.polls + start_result.polls,
            elapsed_seconds=stop_result.elapsed_seconds + start_result.elapsed_seconds,
        )


def _has_status(
    rows: list[dict[str, object]],
    status_keys: tuple[str, ...],
    target_values: frozenset[str],
) -> bool:
    """Check whether any row has a status value in the target set."""
    for row in rows:
        for key in status_keys:
            value = row.get(key)
            if isinstance(value, str) and value in target_values:
                return True
    return False
