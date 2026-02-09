"""Authentication credential types and LTPA login support."""

from __future__ import annotations

import http.cookies
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .exceptions import MQRESTAuthError

if TYPE_CHECKING:
    from collections.abc import Mapping

    from .session import MQRESTTransport

LTPA_COOKIE_NAME = "LtpaToken2"
LTPA_LOGIN_PATH = "/login"
ERROR_LTPA_LOGIN_FAILED = "LTPA login failed."
ERROR_LTPA_TOKEN_MISSING = "LTPA login succeeded but no LtpaToken2 cookie was returned."  # noqa: S105


@dataclass(frozen=True)
class BasicAuth:
    """HTTP Basic authentication credentials.

    Attributes:
        username: Username for HTTP Basic authentication.
        password: Password for HTTP Basic authentication.

    """

    username: str
    password: str


@dataclass(frozen=True)
class LTPAAuth:
    """LTPA token-based authentication credentials.

    The session performs an LTPA login at construction time and uses
    the returned ``LtpaToken2`` cookie for subsequent requests.

    Attributes:
        username: Username for the LTPA login request.
        password: Password for the LTPA login request.

    """

    username: str
    password: str


@dataclass(frozen=True)
class CertificateAuth:
    """Mutual TLS (mTLS) client certificate authentication.

    The client certificate is configured on the transport layer.
    No ``Authorization`` header is sent.

    Attributes:
        cert_path: Path to the client certificate PEM file.
        key_path: Path to the private key PEM file, or ``None``
            if the key is included in the certificate file.

    """

    cert_path: str
    key_path: str | None = None


Credentials = BasicAuth | LTPAAuth | CertificateAuth
"""Type alias for the supported credential types."""


def perform_ltpa_login(  # noqa: PLR0913
    transport: MQRESTTransport,
    rest_base_url: str,
    credentials: LTPAAuth,
    *,
    csrf_token: str | None,
    timeout_seconds: float | None,
    verify_tls: bool,
) -> str:
    """Perform an LTPA login and return the ``LtpaToken2`` token value.

    Args:
        transport: The transport to use for the login POST request.
        rest_base_url: Base URL of the MQ REST API.
        credentials: LTPA credentials containing username and password.
        csrf_token: CSRF token value for the request header.
        timeout_seconds: Request timeout in seconds.
        verify_tls: Whether to verify the server's TLS certificate.

    Returns:
        The ``LtpaToken2`` cookie value string.

    Raises:
        MQRESTAuthError: If the login request fails or the response
            does not contain an ``LtpaToken2`` cookie.

    """
    login_url = f"{rest_base_url}{LTPA_LOGIN_PATH}"
    headers: dict[str, str] = {"Accept": "application/json"}
    if csrf_token is not None:
        headers["ibm-mq-rest-csrf-token"] = csrf_token
    payload: dict[str, object] = {
        "username": credentials.username,
        "password": credentials.password,
    }
    response = transport.post_json(
        login_url,
        payload,
        headers=headers,
        timeout_seconds=timeout_seconds,
        verify_tls=verify_tls,
    )
    if response.status_code >= 400:  # noqa: PLR2004
        raise MQRESTAuthError(
            ERROR_LTPA_LOGIN_FAILED,
            url=login_url,
            status_code=response.status_code,
        )
    token = _extract_ltpa_token(response.headers)
    if token is None:
        raise MQRESTAuthError(
            ERROR_LTPA_TOKEN_MISSING,
            url=login_url,
            status_code=response.status_code,
        )
    return token


def _extract_ltpa_token(headers: Mapping[str, str]) -> str | None:
    """Extract the ``LtpaToken2`` value from response ``Set-Cookie`` headers.

    Uses :class:`http.cookies.SimpleCookie` for robust cookie parsing.

    Args:
        headers: Response headers mapping.

    Returns:
        The token string, or ``None`` if not found.

    """
    set_cookie = headers.get("Set-Cookie") or headers.get("set-cookie")
    if not set_cookie:
        return None
    cookie = http.cookies.SimpleCookie()
    cookie.load(set_cookie)
    morsel = cookie.get(LTPA_COOKIE_NAME)
    if morsel is not None:
        return morsel.value
    return None
