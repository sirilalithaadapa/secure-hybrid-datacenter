from app.security import evaluate


def flow(source, destination, action, port):
    return evaluate({"source": source, "destination": destination, "action": action, "port": port})


def test_internet_to_teaching_allowed():
    assert flow("internet", "teaching", "read", 443)["decision"] == "ALLOW"


def test_teaching_to_database_allowed():
    assert flow("teaching", "database", "read", 5432)["decision"] == "ALLOW"


def test_teaching_to_research_denied():
    assert flow("teaching", "research", "read", 443)["decision"] == "DENY"


def test_internet_to_database_denied():
    assert flow("internet", "database", "read", 5432)["decision"] == "DENY"


def test_unknown_flow_defaults_to_deny():
    assert flow("unknown", "unknown", "read", 443)["decision"] == "DENY"
