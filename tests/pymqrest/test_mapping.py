"""Tests for MQSC <-> snake_case mapping logic."""

from __future__ import annotations

import pytest

import pymqrest.mapping as mapping_module
from pymqrest.mapping import (
    MappingError,
    MappingIssue,
    map_request_attributes,
    map_response_attributes,
    map_response_list,
)

EXPECTED_ISSUE_COUNT = 2


def test_map_request_attributes_translates_keys_and_values() -> None:
    request_attributes = {
        "default_persistence": "def",
        "default_priority": 3,
    }

    mapped_attributes = map_request_attributes("queue", request_attributes)

    assert mapped_attributes == {
        "DEFPSIST": "DEF",
        "DEFPRTY": 3,
    }


def test_map_request_attributes_handles_key_value_map() -> None:
    mapped_attributes = map_request_attributes(
        "channel",
        {"channel_instance_type": "current"},
        strict=True,
    )

    assert mapped_attributes == {"CURRENT": "YES"}


def test_map_request_attributes_key_value_map_unknown_value() -> None:
    with pytest.raises(MappingError) as error_info:
        map_request_attributes(
            "channel",
            {"channel_instance_type": "unknown"},
            strict=True,
        )

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_value"
    assert issue.attribute_name == "channel_instance_type"


def test_map_request_attributes_key_value_map_non_string_value() -> None:
    with pytest.raises(MappingError) as error_info:
        map_request_attributes(
            "channel",
            {"channel_instance_type": 123},
            strict=True,
        )

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_value"
    assert issue.attribute_name == "channel_instance_type"


def test_map_response_attributes_translates_keys_and_values() -> None:
    response_attributes = {
        "DEFPSIST": "NOTFIXED",
        "CURDEPTH": 2,
    }

    mapped_attributes = map_response_attributes("queue", response_attributes)

    assert mapped_attributes == {
        "default_persistence": "not_fixed",
        "current_queue_depth": 2,
    }


def test_map_response_attributes_raises_on_unknown_key() -> None:
    response_attributes = {
        "CURDEPTH": 1,
        "UNKNOWN": 2,
    }

    with pytest.raises(MappingError) as error_info:
        map_response_attributes("queue", response_attributes)

    issues = error_info.value.issues
    assert len(issues) == 1
    issue = issues[0]
    assert issue.reason == "unknown_key"
    assert issue.attribute_name == "UNKNOWN"


def test_map_response_attributes_raises_on_unknown_value() -> None:
    response_attributes = {
        "DEFPSIST": "NOPE",
    }

    with pytest.raises(MappingError) as error_info:
        map_response_attributes("queue", response_attributes)

    issues = error_info.value.issues
    assert len(issues) == 1
    issue = issues[0]
    assert issue.reason == "unknown_value"
    assert issue.attribute_name == "DEFPSIST"


def test_map_response_list_aggregates_errors() -> None:
    response_objects = [
        {"CURDEPTH": 1},
        {"BADKEY": "value"},
        {"DEFPSIST": "NOPE"},
    ]

    with pytest.raises(MappingError) as error_info:
        map_response_list("queue", response_objects)

    issues = error_info.value.issues
    assert len(issues) == EXPECTED_ISSUE_COUNT
    issue_indexes = {issue.object_index for issue in issues}
    assert issue_indexes == {1, 2}


def test_map_response_list_lenient_allows_unknowns() -> None:
    response_objects = [
        {"CURDEPTH": 1},
        {"BADKEY": "value"},
    ]

    mapped_objects = map_response_list("queue", response_objects, strict=False)

    assert mapped_objects[1]["BADKEY"] == "value"


def test_mapping_error_payload_is_json_serializable() -> None:
    response_attributes = {
        "UNKNOWN": b"bytes-value",
    }

    with pytest.raises(MappingError) as error_info:
        map_response_attributes("queue", response_attributes)

    payload = error_info.value.to_payload()
    assert payload[0]["attribute_value"] == "62797465732d76616c7565"


def test_mapping_error_empty_issues_message() -> None:
    error = MappingError([])
    assert str(error) == "Mapping failed with no issues reported."


def test_mapping_error_message_includes_issue_details() -> None:
    issue = MappingIssue(
        direction="request",
        reason="unknown_key",
        attribute_name="ATTRIBUTE",
        attribute_value=123,
        qualifier="queue",
    )
    error = MappingError([issue])
    message = str(error)
    assert "value=123" in message
    assert "qualifier=queue" in message


def test_mapping_error_respects_custom_message() -> None:
    error = MappingError([], message="custom message")
    assert str(error) == "custom message"


def test_map_request_attributes_unknown_qualifier_lenient() -> None:
    mapped_attributes = map_request_attributes(
        "unknown",
        {"attribute": "value"},
        strict=False,
    )
    assert mapped_attributes == {"attribute": "value"}


def test_map_response_attributes_unknown_qualifier_strict() -> None:
    with pytest.raises(MappingError) as error_info:
        map_response_attributes("unknown", {"attribute": "value"})

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_qualifier"


def test_map_response_list_unknown_qualifier_lenient() -> None:
    mapped_objects = map_response_list(
        "unknown",
        [{"attribute": "value"}],
        strict=False,
    )
    assert mapped_objects == [{"attribute": "value"}]


def test_map_response_list_unknown_qualifier_strict() -> None:
    with pytest.raises(MappingError) as error_info:
        map_response_list("unknown", [{"attribute": "value"}], strict=True)

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_qualifier"


def test_mapping_data_invalid_shapes_are_handled(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(mapping_module, "MAPPING_DATA", {"qualifiers": "invalid"})

    mapped_attributes = map_request_attributes("queue", {"attribute": "value"}, strict=False)

    assert mapped_attributes == {"attribute": "value"}


def test_mapping_data_invalid_qualifier_entries_are_ignored(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(mapping_module, "MAPPING_DATA", {"qualifiers": {"queue": "invalid"}})

    mapped_attributes = map_request_attributes("queue", {"attribute": "value"}, strict=False)

    assert mapped_attributes == {"attribute": "value"}


def test_invalid_key_and_value_maps_fall_back_to_empty(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        mapping_module,
        "MAPPING_DATA",
        {"qualifiers": {"queue": {"request_key_map": "invalid", "request_value_map": "invalid"}}},
    )

    mapped_attributes = map_request_attributes("queue", {"attribute": "value"}, strict=False)

    assert mapped_attributes == {"attribute": "value"}


def test_map_value_list_handles_mixed_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        mapping_module,
        "MAPPING_DATA",
        {
            "qualifiers": {
                "queue": {
                    "request_key_map": {"values": "VALUES"},
                    "request_value_map": {"values": {"a": "A", "b": "B"}},
                },
            },
        },
    )

    mapped_attributes = map_request_attributes(
        "queue",
        {"values": ["a", "c", 3]},
        strict=False,
    )

    assert mapped_attributes == {"VALUES": ["A", "c", 3]}


def test_map_value_keeps_non_string_non_list_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        mapping_module,
        "MAPPING_DATA",
        {
            "qualifiers": {
                "queue": {
                    "request_key_map": {"metadata": "METADATA"},
                    "request_value_map": {"metadata": {"a": "A"}},
                },
            },
        },
    )

    mapped_attributes = map_request_attributes(
        "queue",
        {"metadata": {"k": "v"}},
        strict=False,
    )

    assert mapped_attributes == {"METADATA": {"k": "v"}}


def test_mapping_issue_serializes_nested_values() -> None:
    issue = MappingIssue(
        direction="response",
        reason="unknown_value",
        attribute_name="ATTRIBUTE",
        attribute_value={1: ["text", b"bytes", (2, 3), {"nested": complex(1, 2)}]},
        qualifier="queue",
    )

    payload = issue.to_payload()

    assert payload["attribute_value"] == {
        "1": ["text", "6279746573", [2, 3], {"nested": "(1+2j)"}],
    }


def test_map_request_attributes_with_explicit_mapping_data() -> None:
    custom_data: dict[str, object] = {
        "qualifiers": {
            "custom": {
                "request_key_map": {"my_key": "MY_KEY"},
                "request_value_map": {},
            },
        },
    }

    result = map_request_attributes("custom", {"my_key": "val"}, mapping_data=custom_data)

    assert result == {"MY_KEY": "val"}


def test_map_response_attributes_with_explicit_mapping_data() -> None:
    custom_data: dict[str, object] = {
        "qualifiers": {
            "custom": {
                "response_key_map": {"MY_KEY": "my_key"},
                "response_value_map": {},
            },
        },
    }

    result = map_response_attributes("custom", {"MY_KEY": "val"}, mapping_data=custom_data)

    assert result == {"my_key": "val"}


def test_map_response_list_with_explicit_mapping_data() -> None:
    custom_data: dict[str, object] = {
        "qualifiers": {
            "custom": {
                "response_key_map": {"ATTR": "attr"},
                "response_value_map": {},
            },
        },
    }

    result = map_response_list("custom", [{"ATTR": "val"}], mapping_data=custom_data)

    assert result == [{"attr": "val"}]


def test_mapping_data_none_uses_module_default() -> None:
    result = map_request_attributes(
        "queue",
        {"default_persistence": "def"},
        mapping_data=None,
    )

    assert result == {"DEFPSIST": "DEF"}


def test_mapping_issue_serializes_none() -> None:
    issue = MappingIssue(
        direction="response",
        reason="unknown_value",
        attribute_name="ATTRIBUTE",
        attribute_value=None,
        qualifier="queue",
    )

    payload = issue.to_payload()

    assert payload["attribute_value"] is None
