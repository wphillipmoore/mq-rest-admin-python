"""Runtime attribute mapping for MQSC <-> snake_case translations."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Literal, cast

from .mapping_data import MAPPING_DATA

MappingDirection = Literal["request", "response"]
MappingReason = Literal["unknown_key", "unknown_value", "unknown_qualifier"]


@dataclass(frozen=True)
class MappingIssue:
    """Single mapping issue recorded during attribute translation.

    Each issue describes one attribute that could not be fully mapped
    (unknown key, unknown value, or unknown qualifier).

    Attributes:
        direction: Whether the issue occurred during ``"request"`` or
            ``"response"`` mapping.
        reason: Category of the mapping failure — ``"unknown_key"``,
            ``"unknown_value"``, or ``"unknown_qualifier"``.
        attribute_name: The attribute name that triggered the issue.
        attribute_value: The attribute value, if relevant to the issue.
        object_index: Zero-based index within a response list, or
            ``None`` for single-object operations.
        qualifier: The qualifier that was being mapped, or ``None``
            if not applicable.

    """

    direction: MappingDirection
    reason: MappingReason
    attribute_name: str
    attribute_value: object | None = None
    object_index: int | None = None
    qualifier: str | None = None

    def to_payload(self) -> dict[str, object | None]:
        """Return the issue as a JSON-serialisable dict.

        Returns:
            A dict with keys ``direction``, ``reason``,
            ``attribute_name``, ``attribute_value``, ``object_index``,
            and ``qualifier``.

        """
        return {
            "direction": self.direction,
            "reason": self.reason,
            "attribute_name": self.attribute_name,
            "attribute_value": _serialize_value(self.attribute_value),
            "object_index": self.object_index,
            "qualifier": self.qualifier,
        }


class MappingError(Exception):
    """Raised when attribute mapping fails in strict mode.

    Contains one or more :class:`MappingIssue` instances describing
    exactly which attributes could not be mapped and why.

    Attributes:
        issues: Tuple of :class:`MappingIssue` instances captured
            during the failed mapping operation.

    """

    def __init__(self, issues: Sequence[MappingIssue], message: str | None = None) -> None:
        """Initialize a mapping error with the captured issues.

        Args:
            issues: One or more mapping issues that caused the failure.
            message: Optional override message. When ``None``, a message
                is built automatically from the issues.

        """
        self.issues = tuple(issues)
        if message is None:
            message = self._build_message()
        super().__init__(message)

    def _build_message(self) -> str:
        if not self.issues:
            return "Mapping failed with no issues reported."
        issue_lines = []
        for issue in self.issues:
            index_label = "-"
            if issue.object_index is not None:
                index_label = str(issue.object_index)
            qualifier_label = issue.qualifier or "-"
            value_label = "-"
            if issue.attribute_value is not None:
                value_label = repr(issue.attribute_value)
            issue_lines.append(
                " | ".join(
                    [
                        f"index={index_label}",
                        f"qualifier={qualifier_label}",
                        f"direction={issue.direction}",
                        f"reason={issue.reason}",
                        f"attribute={issue.attribute_name}",
                        f"value={value_label}",
                    ],
                ),
            )
        header = f"Mapping failed with {len(self.issues)} issue(s):"
        return "\n".join([header, *issue_lines])

    def to_payload(self) -> list[dict[str, object | None]]:
        """Return mapping issues as JSON-serialisable dicts.

        Returns:
            A list of dicts, one per issue (see
            :meth:`MappingIssue.to_payload`).

        """
        return [issue.to_payload() for issue in self.issues]


def map_request_attributes(
    qualifier: str,
    attributes: Mapping[str, object],
    *,
    strict: bool = True,
) -> dict[str, object]:
    """Map request attributes from ``snake_case`` into MQSC parameter names.

    Translates Python-friendly attribute names and values into the
    native MQSC forms expected by the MQ REST API.

    Args:
        qualifier: The mapping qualifier (e.g. ``"queue"``, ``"channel"``).
            See :doc:`/mappings/index` for available qualifiers.
        attributes: Request attributes keyed by ``snake_case`` names.
        strict: When ``True`` (default), raise :class:`MappingError`
            on any unrecognised key, value, or qualifier. When ``False``,
            pass unrecognised attributes through unchanged.

    Returns:
        A new dict with MQSC parameter names as keys.

    Raises:
        MappingError: If *strict* is ``True`` and any attribute cannot
            be mapped.

    """
    qualifier_data = _get_qualifier_data(qualifier)
    if qualifier_data is None:
        return _handle_unknown_qualifier(
            qualifier,
            attributes,
            direction="request",
            strict=strict,
        )
    return _map_attributes(
        qualifier=qualifier,
        attributes=attributes,
        key_map=_get_key_map(qualifier_data, "request_key_map"),
        key_value_map=_get_key_value_map(qualifier_data, "request_key_value_map"),
        value_map=_get_value_map(qualifier_data, "request_value_map"),
        direction="request",
        strict=strict,
    )


def map_response_attributes(
    qualifier: str,
    attributes: Mapping[str, object],
    *,
    strict: bool = True,
) -> dict[str, object]:
    """Map response attributes from MQSC parameter names to ``snake_case``.

    Translates native MQSC attribute names and values returned by the
    MQ REST API into Python-friendly ``snake_case`` forms.

    Args:
        qualifier: The mapping qualifier (e.g. ``"queue"``, ``"channel"``).
            See :doc:`/mappings/index` for available qualifiers.
        attributes: Response attributes keyed by MQSC parameter names.
        strict: When ``True`` (default), raise :class:`MappingError`
            on any unrecognised key, value, or qualifier. When ``False``,
            pass unrecognised attributes through unchanged.

    Returns:
        A new dict with ``snake_case`` attribute names as keys.

    Raises:
        MappingError: If *strict* is ``True`` and any attribute cannot
            be mapped.

    """
    qualifier_data = _get_qualifier_data(qualifier)
    if qualifier_data is None:
        return _handle_unknown_qualifier(
            qualifier,
            attributes,
            direction="response",
            strict=strict,
        )
    return _map_attributes(
        qualifier=qualifier,
        attributes=attributes,
        key_map=_get_key_map(qualifier_data, "response_key_map"),
        key_value_map={},
        value_map=_get_value_map(qualifier_data, "response_value_map"),
        direction="response",
        strict=strict,
    )


def map_response_list(
    qualifier: str,
    objects: Sequence[Mapping[str, object]],
    *,
    strict: bool = True,
) -> list[dict[str, object]]:
    """Map a list of response objects from MQSC names to ``snake_case``.

    This is the batch equivalent of :func:`map_response_attributes`.
    Each object in the list is mapped independently, and issue tracking
    includes the ``object_index`` so problems can be traced to a
    specific item.

    Args:
        qualifier: The mapping qualifier (e.g. ``"queue"``, ``"channel"``).
            See :doc:`/mappings/index` for available qualifiers.
        objects: Sequence of response attribute dicts to map.
        strict: When ``True`` (default), raise :class:`MappingError`
            if any attribute in any object cannot be mapped. When
            ``False``, pass unrecognised attributes through unchanged.

    Returns:
        A list of dicts with ``snake_case`` attribute names.

    Raises:
        MappingError: If *strict* is ``True`` and any attribute cannot
            be mapped. The error's :attr:`~MappingError.issues` may
            span multiple objects.

    """
    qualifier_data = _get_qualifier_data(qualifier)
    if qualifier_data is None:
        return _handle_unknown_qualifier_list(
            qualifier,
            objects,
            direction="response",
            strict=strict,
        )
    key_map = _get_key_map(qualifier_data, "response_key_map")
    value_map = _get_value_map(qualifier_data, "response_value_map")
    mapped_objects: list[dict[str, object]] = []
    issues: list[MappingIssue] = []
    for object_index, attributes in enumerate(objects):
        mapped_attributes, attribute_issues = _map_attributes_internal(
            qualifier=qualifier,
            attributes=attributes,
            key_map=key_map,
            key_value_map={},
            value_map=value_map,
            direction="response",
            object_index=object_index,
        )
        mapped_objects.append(mapped_attributes)
        issues.extend(attribute_issues)
    if strict and issues:
        raise MappingError(issues)
    return mapped_objects


def _get_qualifier_data(qualifier: str) -> Mapping[str, object] | None:
    qualifiers = MAPPING_DATA.get("qualifiers")
    if not isinstance(qualifiers, Mapping):
        return None
    qualifier_map = cast("Mapping[str, object]", qualifiers)
    qualifier_data = qualifier_map.get(qualifier)
    if isinstance(qualifier_data, Mapping):
        return cast("Mapping[str, object]", qualifier_data)
    return None


def _get_key_map(
    qualifier_data: Mapping[str, object],
    map_name: str,
) -> Mapping[str, str]:
    key_map = qualifier_data.get(map_name)
    if isinstance(key_map, Mapping):
        return cast("Mapping[str, str]", key_map)
    return {}


def _get_value_map(
    qualifier_data: Mapping[str, object],
    map_name: str,
) -> Mapping[str, Mapping[str, str]]:
    value_map = qualifier_data.get(map_name)
    if isinstance(value_map, Mapping):
        return cast("Mapping[str, Mapping[str, str]]", value_map)
    return {}


def _get_key_value_map(
    qualifier_data: Mapping[str, object],
    map_name: str,
) -> Mapping[str, Mapping[str, Mapping[str, str]]]:
    key_value_map = qualifier_data.get(map_name)
    if isinstance(key_value_map, Mapping):
        return cast("Mapping[str, Mapping[str, Mapping[str, str]]]", key_value_map)
    return {}


def _handle_unknown_qualifier(
    qualifier: str,
    attributes: Mapping[str, object],
    *,
    direction: MappingDirection,
    strict: bool,
) -> dict[str, object]:
    if not strict:
        return dict(attributes)
    issues = [
        MappingIssue(
            direction=direction,
            reason="unknown_qualifier",
            attribute_name="*",
            attribute_value=None,
            qualifier=qualifier,
        ),
    ]
    raise MappingError(issues)


def _handle_unknown_qualifier_list(
    qualifier: str,
    objects: Sequence[Mapping[str, object]],
    *,
    direction: MappingDirection,
    strict: bool,
) -> list[dict[str, object]]:
    if not strict:
        return [dict(attributes) for attributes in objects]
    issues = [
        MappingIssue(
            direction=direction,
            reason="unknown_qualifier",
            attribute_name="*",
            attribute_value=None,
            qualifier=qualifier,
        ),
    ]
    raise MappingError(issues)


def _map_attributes(  # noqa: PLR0913
    *,
    qualifier: str,
    attributes: Mapping[str, object],
    key_map: Mapping[str, str],
    key_value_map: Mapping[str, Mapping[str, Mapping[str, str]]],
    value_map: Mapping[str, Mapping[str, str]],
    direction: MappingDirection,
    strict: bool,
) -> dict[str, object]:
    mapped_attributes, issues = _map_attributes_internal(
        qualifier=qualifier,
        attributes=attributes,
        key_map=key_map,
        key_value_map=key_value_map,
        value_map=value_map,
        direction=direction,
        object_index=None,
    )
    if strict and issues:
        raise MappingError(issues)
    return mapped_attributes


def _map_attributes_internal(  # noqa: PLR0913
    *,
    qualifier: str,
    attributes: Mapping[str, object],
    key_map: Mapping[str, str],
    key_value_map: Mapping[str, Mapping[str, Mapping[str, str]]],
    value_map: Mapping[str, Mapping[str, str]],
    direction: MappingDirection,
    object_index: int | None,
) -> tuple[dict[str, object], list[MappingIssue]]:
    mapped_attributes: dict[str, object] = {}
    issues: list[MappingIssue] = []
    for attribute_name, attribute_value in attributes.items():
        if direction == "request":
            value_map_for_key = key_value_map.get(attribute_name)
            if value_map_for_key:
                if isinstance(attribute_value, str):
                    mapping = value_map_for_key.get(attribute_value)
                    if mapping and "key" in mapping and "value" in mapping:
                        mapped_attributes[mapping["key"]] = mapping["value"]
                        continue
                issues.append(
                    MappingIssue(
                        direction=direction,
                        reason="unknown_value",
                        attribute_name=attribute_name,
                        attribute_value=attribute_value,
                        object_index=object_index,
                        qualifier=qualifier,
                    ),
                )
                mapped_attributes[attribute_name] = attribute_value
                continue
        mapped_key = key_map.get(attribute_name)
        if mapped_key is None:
            issues.append(
                MappingIssue(
                    direction=direction,
                    reason="unknown_key",
                    attribute_name=attribute_name,
                    attribute_value=attribute_value,
                    object_index=object_index,
                    qualifier=qualifier,
                ),
            )
            mapped_attributes[attribute_name] = attribute_value
            continue
        mapped_value, value_issues = _map_value(
            qualifier=qualifier,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            value_map=value_map,
            direction=direction,
            object_index=object_index,
        )
        mapped_attributes[mapped_key] = mapped_value
        issues.extend(value_issues)
    return mapped_attributes, issues


def _map_value(  # noqa: PLR0913
    *,
    qualifier: str,
    attribute_name: str,
    attribute_value: object,
    value_map: Mapping[str, Mapping[str, str]],
    direction: MappingDirection,
    object_index: int | None,
) -> tuple[object, list[MappingIssue]]:
    value_mappings = value_map.get(attribute_name)
    if not value_mappings:
        return attribute_value, []
    if isinstance(attribute_value, str):
        mapped_value = value_mappings.get(attribute_value)
        if mapped_value is None:
            return (
                attribute_value,
                [
                    MappingIssue(
                        direction=direction,
                        reason="unknown_value",
                        attribute_name=attribute_name,
                        attribute_value=attribute_value,
                        object_index=object_index,
                        qualifier=qualifier,
                    ),
                ],
            )
        return mapped_value, []
    if isinstance(attribute_value, list):
        return _map_value_list(
            qualifier=qualifier,
            attribute_name=attribute_name,
            attribute_values=cast("list[object]", attribute_value),
            value_mappings=value_mappings,
            direction=direction,
            object_index=object_index,
        )
    return attribute_value, []


def _map_value_list(  # noqa: PLR0913
    *,
    qualifier: str,
    attribute_name: str,
    attribute_values: list[object],
    value_mappings: Mapping[str, str],
    direction: MappingDirection,
    object_index: int | None,
) -> tuple[list[object], list[MappingIssue]]:
    mapped_values: list[object] = []
    issues: list[MappingIssue] = []
    for attribute_value in attribute_values:
        if isinstance(attribute_value, str):
            mapped_value = value_mappings.get(attribute_value)
            if mapped_value is None:
                issues.append(
                    MappingIssue(
                        direction=direction,
                        reason="unknown_value",
                        attribute_name=attribute_name,
                        attribute_value=attribute_value,
                        object_index=object_index,
                        qualifier=qualifier,
                    ),
                )
                mapped_values.append(attribute_value)
                continue
            mapped_values.append(mapped_value)
            continue
        mapped_values.append(attribute_value)
    return mapped_values, issues


def _serialize_value(value: object | None) -> object | None:
    if value is None:
        serialized: object | None = None
    elif isinstance(value, (str, int, float, bool)):
        serialized = value
    elif isinstance(value, bytes):
        serialized = value.hex()
    elif isinstance(value, (list, tuple)):
        serialized = [_serialize_value(item) for item in value]
    elif isinstance(value, dict):
        serialized = {str(key): _serialize_value(item) for key, item in value.items()}
    else:
        serialized = repr(value)
    return serialized
