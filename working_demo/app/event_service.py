from datetime import datetime, timezone
from typing import Any


def security_event(request: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": request.get("source"),
        "destination": request.get("destination"),
        "action": request.get("action"),
        "port": request.get("port"),
        "decision": result.get("decision"),
        "rule": result.get("rule", {}).get("name") if isinstance(result.get("rule"), dict) else result.get("rule"),
        "reason": result.get("reason"),
    }
