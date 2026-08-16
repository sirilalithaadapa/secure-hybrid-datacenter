from app.security import evaluate


def test_default_deny():
    result = evaluate({"source": "internet", "destination": "database", "action": "read", "port": 5432})
    assert result["decision"] == "DENY"


def test_teaching_database_allowed():
    result = evaluate({"source": "teaching", "destination": "database", "action": "read", "port": 5432})
    assert result["decision"] == "ALLOW"


def test_cross_zone_denied():
    result = evaluate({"source": "teaching", "destination": "research", "action": "read", "port": 443})
    assert result["decision"] == "DENY"


def test_dns_allowed():
    result = evaluate({"source": "teaching", "destination": "dns", "action": "resolve", "port": 53})
    assert result["decision"] == "ALLOW"
