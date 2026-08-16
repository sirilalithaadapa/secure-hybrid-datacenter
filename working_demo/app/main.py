from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from .security import evaluate, load_policy

BASE = Path(__file__).resolve().parent

app = FastAPI(
    title="Secure Hybrid Data Center Security Platform",
    version="2.0.0",
    description="Interactive proof-of-concept for zero-trust policy enforcement and hybrid data-center segmentation.",
)
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


@app.get("/", response_class=HTMLResponse)
async def home() -> HTMLResponse:
    return HTMLResponse((BASE / "static" / "index.html").read_text(encoding="utf-8"))


@app.get("/health")
async def health() -> dict:
    return {"status": "healthy", "service": "hybrid-security-demo", "time": now()}


@app.get("/api/policy")
async def policy() -> dict:
    return load_policy()


@app.post("/api/check")
async def check(request: Request) -> dict:
    body = await request.json()
    required = ["source", "destination", "action"]
    missing = [key for key in required if key not in body]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing fields: {', '.join(missing)}")
    result = evaluate(body)
    return {"timestamp": now(), "request": body, **result}


def protected(source: str, destination: str, action: str, port: int, service: str):
    result = evaluate({"source": source, "destination": destination, "action": action, "port": port})
    if result["decision"] != "ALLOW":
        return JSONResponse(status_code=403, content={"service": service, "status": "BLOCKED", **result})
    return {"service": service, "status": "ACCESS_GRANTED", "message": f"{service.title()} access simulated successfully.", "policy": result}


@app.get("/api/service/teaching")
async def teaching(request: Request):
    return protected(request.headers.get("X-Demo-Source", "unknown"), "teaching", "read", 443, "teaching")


@app.get("/api/service/research")
async def research(request: Request):
    return protected(request.headers.get("X-Demo-Source", "unknown"), "research", "read", 443, "research")


@app.get("/api/service/database")
async def database(request: Request):
    return protected(request.headers.get("X-Demo-Source", "unknown"), "database", "read", 5432, "database")


@app.get("/api/scenarios")
async def scenarios() -> list[dict]:
    return [
        {"name": "Internet → Teaching", "source": "internet", "destination": "teaching", "action": "read", "port": 443, "expected": "ALLOW"},
        {"name": "Teaching → Database", "source": "teaching", "destination": "database", "action": "read", "port": 5432, "expected": "ALLOW"},
        {"name": "Teaching → Research", "source": "teaching", "destination": "research", "action": "read", "port": 443, "expected": "DENY"},
        {"name": "Research → Teaching", "source": "research", "destination": "teaching", "action": "read", "port": 443, "expected": "DENY"},
        {"name": "Internet → Database", "source": "internet", "destination": "database", "action": "read", "port": 5432, "expected": "DENY"},
        {"name": "Developer → Security Admin", "source": "developer", "destination": "security-admin", "action": "admin", "port": 443, "expected": "DENY"},
        {"name": "Teaching → DNS", "source": "teaching", "destination": "dns", "action": "resolve", "port": 53, "expected": "ALLOW"},
    ]
