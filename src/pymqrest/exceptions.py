"""MQ REST exception definitions."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping


class MQRESTError(Exception):
    """Base error for MQ REST session failures."""


class MQRESTTransportError(MQRESTError):
    """Raised when the transport fails to reach the MQ REST endpoint."""

    def __init__(self, message: str, *, url: str) -> None:
        super().__init__(message)
        self.url = url


class MQRESTResponseError(MQRESTError):
    """Raised when the MQ REST response is malformed or unexpected."""

    def __init__(self, message: str, *, response_text: str | None = None) -> None:
        super().__init__(message)
        self.response_text = response_text


class MQRESTCommandError(MQRESTError):
    """Raised when the MQ REST response indicates command failure."""

    def __init__(
        self,
        message: str,
        *,
        payload: Mapping[str, object],
        status_code: int | None = None,
    ) -> None:
        super().__init__(message)
        self.payload = dict(payload)
        self.status_code = status_code
