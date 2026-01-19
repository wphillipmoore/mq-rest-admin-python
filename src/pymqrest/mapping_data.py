"""Precompiled mapping data for MQSC <-> snake_case translations."""

from __future__ import annotations

MAPPING_DATA = {
    "commands": {
        "DISPLAY CHANNEL": {"qualifier": "channel", "status": "provisional"},
        "DISPLAY QMGR": {"qualifier": "qmgr", "status": "provisional"},
        "DISPLAY QUEUE": {"qualifier": "queue", "status": "provisional"},
    },
    "qualifiers": {
        "channel": {
            "request_key_map": {"channel_type": "CHLTYPE"},
            "request_value_map": {},
            "response_key_map": {"CHLTYPE": "channel_type"},
            "response_value_map": {},
        },
        "qmgr": {
            "request_key_map": {"qmgr_name": "QMNAME"},
            "request_value_map": {},
            "response_key_map": {"QMNAME": "qmgr_name"},
            "response_value_map": {},
        },
        "queue": {
            "request_key_map": {
                "current_q_depth": "CURDEPTH",
                "def_persistence": "DEFPSIST",
            },
            "request_value_map": {"def_persistence": {"def": "DEF", "not_fixed": "NOTFIXED"}},
            "response_key_map": {
                "CURDEPTH": "current_q_depth",
                "DEFPSIST": "def_persistence",
            },
            "response_value_map": {"DEFPSIST": {"DEF": "def", "NOTFIXED": "not_fixed"}},
        },
    },
    "version": 1,
}
