"""Tests for MQSC <-> snake_case mapping logic."""

from __future__ import annotations

import pytest

from pymqrest.mapping import (
    MappingError,
    map_request_attributes,
    map_response_attributes,
    map_response_list,
)


def test_map_request_attributes_translates_keys_and_values() -> None:
    request_attributes = {
        "def_persistence": "def",
        "current_q_depth": 10,
    }

    mapped_attributes = map_request_attributes("queue", request_attributes)

    assert mapped_attributes == {
        "DEFPSIST": "DEF",
        "CURDEPTH": 10,
    }


def test_map_response_attributes_translates_keys_and_values() -> None:
    response_attributes = {
        "DEFPSIST": "NOTFIXED",
        "CURDEPTH": 2,
    }

    mapped_attributes = map_response_attributes("queue", response_attributes)

    assert mapped_attributes == {
        "def_persistence": "not_fixed",
        "current_q_depth": 2,
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
    assert len(issues) == 2
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
