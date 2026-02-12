"""pymqrest runtime package."""

from importlib.metadata import version

from ._mapping_merge import MappingOverrideMode
from .auth import BasicAuth, CertificateAuth, Credentials, LTPAAuth
from .ensure import EnsureAction, EnsureResult
from .exceptions import (
    MQRESTAuthError,
    MQRESTCommandError,
    MQRESTError,
    MQRESTResponseError,
    MQRESTTimeoutError,
    MQRESTTransportError,
)
from .mapping import (
    MappingError,
    MappingIssue,
    map_request_attributes,
    map_response_attributes,
    map_response_list,
)
from .session import MQRESTSession
from .sync import SyncConfig, SyncOperation, SyncResult

__version__ = version("pymqrest")

__all__ = [
    "BasicAuth",
    "CertificateAuth",
    "Credentials",
    "EnsureAction",
    "EnsureResult",
    "LTPAAuth",
    "MQRESTAuthError",
    "MQRESTCommandError",
    "MQRESTError",
    "MQRESTResponseError",
    "MQRESTSession",
    "MQRESTTimeoutError",
    "MQRESTTransportError",
    "MappingError",
    "MappingIssue",
    "MappingOverrideMode",
    "SyncConfig",
    "SyncOperation",
    "SyncResult",
    "__version__",
    "map_request_attributes",
    "map_response_attributes",
    "map_response_list",
]
