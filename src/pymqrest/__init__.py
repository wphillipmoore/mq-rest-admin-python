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
    "MQRESTTransportError",
    "MappingError",
    "MappingIssue",
    "MappingOverrideMode",
    "__version__",
    "map_request_attributes",
    "map_response_attributes",
    "map_response_list",
]
