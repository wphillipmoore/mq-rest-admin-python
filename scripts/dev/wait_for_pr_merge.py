#!/usr/bin/env python3
"""Wait for a GitHub PR to merge, failing on timeout or CI failures."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from typing import Any

FAIL_CONCLUSIONS = {
    "ACTION_REQUIRED",
    "CANCELLED",
    "FAILURE",
    "STARTUP_FAILURE",
    "TIMED_OUT",
}


def _run_gh(args: list[str]) -> dict[str, Any]:
    result = subprocess.run(  # noqa: S603
        ["gh", *args],  # noqa: S607
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or "gh command failed"
        raise RuntimeError(message)
    payload = result.stdout.strip()
    if not payload:
        message = "gh command returned empty output"
        raise RuntimeError(message)
    return json.loads(payload)


def _fetch_pr(pr: str, repo: str | None) -> dict[str, Any]:
    args = [
        "pr",
        "view",
        pr,
        "--json",
        "state,autoMergeRequest,mergeable,statusCheckRollup",
    ]
    if repo:
        args.extend(["--repo", repo])
    return _run_gh(args)


def _summarize_failures(checks: list[dict[str, Any]]) -> list[str]:
    failures = []
    for check in checks:
        name = check.get("name") or "unknown"
        status = check.get("status") or "UNKNOWN"
        conclusion = check.get("conclusion") or "UNKNOWN"
        if status == "COMPLETED" and conclusion in FAIL_CONCLUSIONS:
            failures.append(f"{name} ({conclusion})")
    return failures


def _summarize_pending(checks: list[dict[str, Any]]) -> list[str]:
    pending = []
    for check in checks:
        name = check.get("name") or "unknown"
        status = check.get("status") or "UNKNOWN"
        conclusion = check.get("conclusion") or "UNKNOWN"
        if status != "COMPLETED":
            pending.append(f"{name} ({status})")
        elif conclusion == "NEUTRAL":
            pending.append(f"{name} ({conclusion})")
    return pending


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pr", help="Pull request number or URL.")
    parser.add_argument(
        "--repo",
        help="GitHub repository in owner/name form.",
        default=None,
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=600,
        help="Maximum wait time before failing.",
    )
    parser.add_argument(
        "--poll-seconds",
        type=int,
        default=20,
        help="Polling interval in seconds.",
    )
    args = parser.parse_args()

    deadline = time.monotonic() + args.timeout_seconds
    attempt = 0

    while True:
        attempt += 1
        data = _fetch_pr(args.pr, args.repo)
        state = data.get("state")
        checks = data.get("statusCheckRollup") or []

        if state == "MERGED":
            print("PR merged.")
            return 0
        if state == "CLOSED":
            print("PR closed without merge.")
            return 2

        failures = _summarize_failures(checks)
        if failures:
            print("CI failures detected:")
            for failure in failures:
                print(f"- {failure}")
            return 3

        pending = _summarize_pending(checks)
        if pending:
            print(f"[{attempt}] Waiting on checks: {', '.join(pending)}")
        else:
            auto_merge = data.get("autoMergeRequest")
            if auto_merge:
                print(f"[{attempt}] Checks complete; waiting on auto-merge.")
            else:
                print(f"[{attempt}] Checks complete; waiting for merge.")

        if time.monotonic() >= deadline:
            print("Timeout waiting for PR to merge.")
            return 1

        time.sleep(args.poll_seconds)


if __name__ == "__main__":
    raise SystemExit(main())
