from app.main import evaluate


def test_internet_to_teaching_allowed():
    result = evaluate("internet", "teaching", "read", 443)
    assert result["decision"] == "ALLOW"


def test_teaching_to_database_allowed():
    result = evaluate("teaching", "database", "read", 5432)
    assert result["decision"] == "ALLOW"


def test_teaching_to_research_denied():
    result = evaluate("teaching", "research", "read", 443)
    assert result["decision"] == "DENY"


def test_internet_to_database_denied():
    result = evaluate("internet", "database", "read", 5432)
    assert result["decision"] == "DENY"


def test_unknown_flow_defaults_to_deny():
    result = evaluate("unknown", "unknown", "read", 443)
    assert result["decision"] == "DENY"
