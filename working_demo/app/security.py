from __future__ import annotations

from pathlib import Path
import json
from typing import Any

POLICY_PATH = Path(__file__).with_name("policy.json")


def load_policy() -> dict[str, Any]:
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def _matches(rule: dict[str, Any], request: dict[str, Any]) -> bool:
    for key in ("source", "destination", "action"):
        if rule.get(key) not in (None, "*", request.get(key)):
            return False
    ports = rule.get("ports")
    if ports is not None and request.get("port") not in ports:
        return False
    return True


def evaluate(request: dict[str, Any]) -> dict[str, Any]:
    policy = load_policy()
    for rule in policy.get("deny", []):
        if _matches(rule, request):
            return {"decision": "DENY", "reason": rule.get("reason", "Explicit deny rule"), "rule": rule}
    for rule in policy.get("allow", []):
        if _matches(rule, request):
            return {"decision": "ALLOW", "reason": rule.get("reason", "Explicit allow rule"), "rule": rule}
    return {"decision": "DENY", "reason": "No explicit allow rule matched; default-deny policy applied", "rule": None}
