"""Runtime attribute mapping for MQSC <-> snake_case translations."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Literal

from .mapping_data import MAPPING_DATA

MappingDirection = Literal["request", "response"]
MappingReason = Literal["unknown_key", "unknown_value", "unknown_qualifier"]


@dataclass(frozen=True)
class MappingIssue:
    direction: MappingDirection
    reason: MappingReason
    attribute_name: str
    attribute_value: object | None = None
    object_index: int | None = None
    qualifier: str | None = None

    def to_payload(self) -> dict[str, object | None]:
        return {
            "direction": self.direction,
            "reason": self.reason,
            "attribute_name": self.attribute_name,
            "attribute_value": _serialize_value(self.attribute_value),
            "object_index": self.object_index,
            "qualifier": self.qualifier,
        }


class MappingError(Exception):
    def __init__(self, issues: Sequence[MappingIssue], message: str | None = None) -> None:
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
                    ]
                )
            )
        header = f"Mapping failed with {len(self.issues)} issue(s):"
        return "\n".join([header, *issue_lines])

    def to_payload(self) -> list[dict[str, object | None]]:
        return [issue.to_payload() for issue in self.issues]


def map_request_attributes(
    qualifier: str,
    attributes: Mapping[str, object],
    *,
    strict: bool = True,
) -> dict[str, object]:
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
    qualifier_data = qualifiers.get(qualifier)
    if isinstance(qualifier_data, Mapping):
        return qualifier_data
    return None


def _get_key_map(
    qualifier_data: Mapping[str, object],
    map_name: str,
) -> Mapping[str, str]:
    key_map = qualifier_data.get(map_name, {})
    if isinstance(key_map, Mapping):
        return key_map
    return {}


def _get_value_map(
    qualifier_data: Mapping[str, object],
    map_name: str,
) -> Mapping[str, Mapping[str, str]]:
    value_map = qualifier_data.get(map_name, {})
    if isinstance(value_map, Mapping):
        return value_map
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
        )
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
        )
    ]
    raise MappingError(issues)


def _map_attributes(
    *,
    qualifier: str,
    attributes: Mapping[str, object],
    key_map: Mapping[str, str],
    value_map: Mapping[str, Mapping[str, str]],
    direction: MappingDirection,
    strict: bool,
) -> dict[str, object]:
    mapped_attributes, issues = _map_attributes_internal(
        qualifier=qualifier,
        attributes=attributes,
        key_map=key_map,
        value_map=value_map,
        direction=direction,
        object_index=None,
    )
    if strict and issues:
        raise MappingError(issues)
    return mapped_attributes


def _map_attributes_internal(
    *,
    qualifier: str,
    attributes: Mapping[str, object],
    key_map: Mapping[str, str],
    value_map: Mapping[str, Mapping[str, str]],
    direction: MappingDirection,
    object_index: int | None,
) -> tuple[dict[str, object], list[MappingIssue]]:
    mapped_attributes: dict[str, object] = {}
    issues: list[MappingIssue] = []
    for attribute_name, attribute_value in attributes.items():
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
                )
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


def _map_value(
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
                    )
                ],
            )
        return mapped_value, []
    if isinstance(attribute_value, list):
        return _map_value_list(
            qualifier=qualifier,
            attribute_name=attribute_name,
            attribute_values=attribute_value,
            value_mappings=value_mappings,
            direction=direction,
            object_index=object_index,
        )
    return attribute_value, []


def _map_value_list(
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
                    )
                )
                mapped_values.append(attribute_value)
                continue
            mapped_values.append(mapped_value)
            continue
        mapped_values.append(attribute_value)
    return mapped_values, issues


def _serialize_value(value: object | None) -> object | None:
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, list):
        return [_serialize_value(item) for item in value]
    if isinstance(value, tuple):
        return [_serialize_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _serialize_value(item) for key, item in value.items()}
    return repr(value)
