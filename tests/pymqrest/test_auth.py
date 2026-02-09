"""Tests for authentication credential types and LTPA login."""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

import pytest

from pymqrest.auth import (
    BasicAuth,
    CertificateAuth,
    LTPAAuth,
    _extract_ltpa_token,
    perform_ltpa_login,
)
from pymqrest.exceptions import MQRESTAuthError
from pymqrest.session import TransportResponse

if TYPE_CHECKING:
    from collections.abc import Mapping

TEST_PASSWORD = "secret"
STATUS_OK = 200
STATUS_UNAUTHORIZED = 401


class FakeLoginTransport:
    def __init__(self, response: TransportResponse) -> None:
        self.response = response
        self.recorded_url: str | None = None
        self.recorded_payload: dict[str, object] | None = None
        self.recorded_headers: dict[str, str] | None = None

    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse:
        _ = timeout_seconds
        _ = verify_tls
        self.recorded_url = url
        self.recorded_payload = dict(payload)
        self.recorded_headers = dict(headers)
        return self.response


# -- Credential dataclass construction and immutability --


def test_basic_auth_construction() -> None:
    cred = BasicAuth(username="user", password=TEST_PASSWORD)
    assert cred.username == "user"
    assert cred.password == TEST_PASSWORD


def test_basic_auth_is_frozen() -> None:
    cred = BasicAuth("user", TEST_PASSWORD)
    with pytest.raises(dataclasses.FrozenInstanceError):
        cred.username = "other"  # type: ignore[misc]


def test_ltpa_auth_construction() -> None:
    cred = LTPAAuth(username="user", password=TEST_PASSWORD)
    assert cred.username == "user"
    assert cred.password == TEST_PASSWORD


def test_ltpa_auth_is_frozen() -> None:
    cred = LTPAAuth("user", TEST_PASSWORD)
    with pytest.raises(dataclasses.FrozenInstanceError):
        cred.username = "other"  # type: ignore[misc]


def test_certificate_auth_construction() -> None:
    cred = CertificateAuth(cert_path="/cert.pem", key_path="/key.pem")
    assert cred.cert_path == "/cert.pem"
    assert cred.key_path == "/key.pem"


def test_certificate_auth_key_path_optional() -> None:
    cred = CertificateAuth(cert_path="/combined.pem")
    assert cred.cert_path == "/combined.pem"
    assert cred.key_path is None


def test_certificate_auth_is_frozen() -> None:
    cred = CertificateAuth("/cert.pem", "/key.pem")
    with pytest.raises(dataclasses.FrozenInstanceError):
        cred.cert_path = "/other.pem"  # type: ignore[misc]


# -- perform_ltpa_login success --


def test_perform_ltpa_login_success() -> None:
    transport = FakeLoginTransport(
        TransportResponse(
            status_code=STATUS_OK,
            text="",
            headers={"Set-Cookie": "LtpaToken2=abc123; Path=/; HttpOnly"},
        ),
    )

    token = perform_ltpa_login(
        transport,
        "https://example.invalid/ibmmq/rest/v2",
        LTPAAuth("user", TEST_PASSWORD),
        csrf_token="local",
        timeout_seconds=30.0,
        verify_tls=False,
    )

    assert token == "abc123"
    assert transport.recorded_url == "https://example.invalid/ibmmq/rest/v2/login"
    assert transport.recorded_payload == {"username": "user", "password": TEST_PASSWORD}
    assert transport.recorded_headers is not None
    assert transport.recorded_headers["ibm-mq-rest-csrf-token"] == "local"


def test_perform_ltpa_login_without_csrf_token() -> None:
    transport = FakeLoginTransport(
        TransportResponse(
            status_code=STATUS_OK,
            text="",
            headers={"Set-Cookie": "LtpaToken2=token_value; Path=/"},
        ),
    )

    token = perform_ltpa_login(
        transport,
        "https://example.invalid/ibmmq/rest/v2",
        LTPAAuth("user", TEST_PASSWORD),
        csrf_token=None,
        timeout_seconds=30.0,
        verify_tls=False,
    )

    assert token == "token_value"
    assert transport.recorded_headers is not None
    assert "ibm-mq-rest-csrf-token" not in transport.recorded_headers


# -- perform_ltpa_login failures --


def test_perform_ltpa_login_http_error_raises() -> None:
    transport = FakeLoginTransport(
        TransportResponse(
            status_code=STATUS_UNAUTHORIZED,
            text='{"error": "bad credentials"}',
            headers={},
        ),
    )

    with pytest.raises(MQRESTAuthError) as excinfo:
        perform_ltpa_login(
            transport,
            "https://example.invalid/ibmmq/rest/v2",
            LTPAAuth("user", TEST_PASSWORD),
            csrf_token="local",
            timeout_seconds=30.0,
            verify_tls=False,
        )

    assert excinfo.value.url == "https://example.invalid/ibmmq/rest/v2/login"
    assert excinfo.value.status_code == STATUS_UNAUTHORIZED


def test_perform_ltpa_login_missing_token_raises() -> None:
    transport = FakeLoginTransport(
        TransportResponse(
            status_code=STATUS_OK,
            text="",
            headers={"Set-Cookie": "SomeOtherCookie=value; Path=/"},
        ),
    )

    with pytest.raises(MQRESTAuthError) as excinfo:
        perform_ltpa_login(
            transport,
            "https://example.invalid/ibmmq/rest/v2",
            LTPAAuth("user", TEST_PASSWORD),
            csrf_token="local",
            timeout_seconds=30.0,
            verify_tls=False,
        )

    assert excinfo.value.url == "https://example.invalid/ibmmq/rest/v2/login"
    assert excinfo.value.status_code == STATUS_OK


def test_perform_ltpa_login_no_set_cookie_raises() -> None:
    transport = FakeLoginTransport(
        TransportResponse(
            status_code=STATUS_OK,
            text="",
            headers={},
        ),
    )

    with pytest.raises(MQRESTAuthError):
        perform_ltpa_login(
            transport,
            "https://example.invalid/ibmmq/rest/v2",
            LTPAAuth("user", TEST_PASSWORD),
            csrf_token="local",
            timeout_seconds=30.0,
            verify_tls=False,
        )


# -- _extract_ltpa_token edge cases --


def test_extract_ltpa_token_with_multiple_cookies() -> None:
    headers = {"Set-Cookie": "Other=x; Path=/, LtpaToken2=multi_tok; Path=/; Secure"}
    assert _extract_ltpa_token(headers) == "multi_tok"


def test_extract_ltpa_token_no_match() -> None:
    headers = {"Set-Cookie": "SessionId=abc; Path=/"}
    assert _extract_ltpa_token(headers) is None


def test_extract_ltpa_token_empty_set_cookie() -> None:
    headers = {"Set-Cookie": ""}
    assert _extract_ltpa_token(headers) is None


def test_extract_ltpa_token_no_headers() -> None:
    assert _extract_ltpa_token({}) is None


def test_extract_ltpa_token_lowercase_header() -> None:
    headers = {"set-cookie": "LtpaToken2=lower_tok; Path=/"}
    assert _extract_ltpa_token(headers) == "lower_tok"
