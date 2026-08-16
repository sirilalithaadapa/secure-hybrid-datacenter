from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from datetime import datetime, timezone
import json

BASE = Path(__file__).resolve().parent
POLICY_FILE = BASE / "policy.json"

app = FastAPI(
    title="Hybrid Security Demo",
    version="1.0.0",
    description="Interactive demonstration of IAM + VPC + Kubernetes-style segmentation."
)

app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")


def load_policy():
    return json.loads(POLICY_FILE.read_text())


def evaluate(source, destination, action, port=None):
    policy = load_policy()

    for rule in policy["allow"]:
        if (
            rule["source"] == source
            and rule["destination"] == destination
            and rule["action"] == action
            and (rule.get("port") is None or rule.get("port") == port)
        ):
            return {"decision": "ALLOW", "reason": rule["reason"], "rule": rule["name"]}

    for rule in policy["deny"]:
        if (
            (rule["source"] == source or rule["source"] == "*")
            and (rule["destination"] == destination or rule["destination"] == "*")
            and (rule["action"] == action or rule["action"] == "*")
        ):
            return {"decision": "DENY", "reason": rule["reason"], "rule": rule["name"]}

    return {"decision": "DENY", "reason": "Default deny: no explicit allow rule exists.", "rule": "DEFAULT_DENY"}


@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse((BASE / "static" / "index.html").read_text())


@app.get("/health")
async def health():
    return {"status": "healthy", "service": "hybrid-security-demo", "time": datetime.now(timezone.utc).isoformat()}


@app.get("/api/policy")
async def policy():
    return load_policy()


@app.post("/api/check")
async def check(request: Request):
    body = await request.json()
    required = ["source", "destination", "action"]
    missing = [x for x in required if x not in body]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing fields: {', '.join(missing)}")
    result = evaluate(body["source"], body["destination"], body["action"], body.get("port"))
    return {"timestamp": datetime.now(timezone.utc).isoformat(), "request": body, **result}


@app.get("/api/service/teaching")
async def teaching(request: Request):
    source = request.headers.get("X-Demo-Source", "unknown")
    result = evaluate(source, "teaching", "read", 443)
    if result["decision"] != "ALLOW":
        return JSONResponse(status_code=403, content={"service": "teaching", "status": "BLOCKED", **result})
    return {"service": "teaching", "status": "ACCESS_GRANTED", "message": "Teaching application data returned.", "policy": result}


@app.get("/api/service/research")
async def research(request: Request):
    source = request.headers.get("X-Demo-Source", "unknown")
    result = evaluate(source, "research", "read", 443)
    if result["decision"] != "ALLOW":
        return JSONResponse(status_code=403, content={"service": "research", "status": "BLOCKED", **result})
    return {"service": "research", "status": "ACCESS_GRANTED", "message": "Research application data returned.", "policy": result}


@app.get("/api/service/database")
async def database(request: Request):
    source = request.headers.get("X-Demo-Source", "unknown")
    result = evaluate(source, "database", "read", 5432)
    if result["decision"] != "ALLOW":
        return JSONResponse(status_code=403, content={"service": "database", "status": "BLOCKED", **result})
    return {"service": "database", "status": "ACCESS_GRANTED", "message": "Database query simulated successfully.", "policy": result}


@app.get("/api/scenarios")
async def scenarios():
    return [
        {"name": "Internet -> Teaching", "source": "internet", "destination": "teaching", "action": "read", "port": 443},
        {"name": "Teaching -> Database", "source": "teaching", "destination": "database", "action": "read", "port": 5432},
        {"name": "Teaching -> Research", "source": "teaching", "destination": "research", "action": "read", "port": 443},
        {"name": "Research -> Teaching", "source": "research", "destination": "teaching", "action": "read", "port": 443},
        {"name": "Developer -> Security Admin API", "source": "developer", "destination": "security-admin", "action": "admin", "port": 443},
        {"name": "Workload -> DNS", "source": "teaching", "destination": "dns", "action": "resolve", "port": 53},
    ]
