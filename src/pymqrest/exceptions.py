"""MQ REST exception definitions."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping


class MQRESTError(Exception):
    """Base error for all MQ REST session failures.

    All pymqrest exceptions inherit from this class, so
    ``except MQRESTError`` catches every error raised by the library.
    """


class MQRESTTransportError(MQRESTError):
    """Raised when the transport fails to reach the MQ REST endpoint.

    This typically indicates a network-level problem such as a connection
    refusal, DNS failure, or TLS handshake error.

    Attributes:
        url: The endpoint URL that could not be reached.

    """

    def __init__(self, message: str, *, url: str) -> None:
        """Initialize with the failing endpoint URL.

        Args:
            message: Human-readable error description.
            url: The MQ REST endpoint URL that the transport tried to reach.

        """
        super().__init__(message)
        self.url = url


class MQRESTResponseError(MQRESTError):
    """Raised when the MQ REST response is malformed or unexpected.

    This indicates the server returned a response that could not be
    parsed as valid JSON or did not conform to the expected
    ``runCommandJSON`` response structure.

    Attributes:
        response_text: The raw response body, if available.

    """

    def __init__(self, message: str, *, response_text: str | None = None) -> None:
        """Initialize with optional response payload text.

        Args:
            message: Human-readable error description.
            response_text: The raw HTTP response body, or ``None`` if
                unavailable.

        """
        super().__init__(message)
        self.response_text = response_text


class MQRESTCommandError(MQRESTError):
    """Raised when the MQ REST response indicates MQSC command failure.

    The server returned a valid JSON response, but the completion or
    reason codes indicate the MQSC command did not succeed.

    Attributes:
        payload: The full JSON response payload as a dict.
        status_code: The HTTP status code, or ``None`` if unavailable.

    """

    def __init__(
        self,
        message: str,
        *,
        payload: Mapping[str, object],
        status_code: int | None = None,
    ) -> None:
        """Initialize with response payload and HTTP status.

        Args:
            message: Human-readable error description including
                completion and reason codes.
            payload: The full JSON response payload from the MQ REST API.
            status_code: The HTTP status code from the response.

        """
        super().__init__(message)
        self.payload = dict(payload)
        self.status_code = status_code
