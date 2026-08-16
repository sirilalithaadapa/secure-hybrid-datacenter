# 🛡️ Secure Hybrid Data Center Security Platform

[![CI](https://github.com/sirilalithaadapa/secure-hybrid-datacenter/actions/workflows/ci.yml/badge.svg)](https://github.com/sirilalithaadapa/secure-hybrid-datacenter/actions/workflows/ci.yml)

> **Cybersecurity engineering project — Hybrid Cloud • Zero Trust • Kubernetes Security • Policy Enforcement**

A working cybersecurity proof-of-concept for a college hybrid data-center environment. It combines AWS network-security architecture, Kubernetes workload isolation, IAM least privilege, threat modeling, automated security tests, and a FastAPI policy-enforcement platform with a professional security dashboard.

## 🎯 What this project demonstrates

- **Hybrid connectivity** — AWS cloud ↔ private data center reference architecture
- **AWS VPC segmentation** — isolated trust zones, subnets and controlled routing
- **Transit Gateway** — centralized hybrid routing model
- **Security Groups** — least-privilege application/database traffic paths
- **IAM** — role/policy examples following least privilege
- **Kubernetes NetworkPolicies** — namespace and workload isolation
- **Default deny** — unknown traffic is denied unless explicitly allowed
- **Network visibility** — VPC Flow Logs reference configuration
- **Threat modeling** — threat-to-control analysis
- **FastAPI** — server-side policy evaluation and protected demo endpoints
- **HTML/CSS/JavaScript** — security operations dashboard
- **Docker** — reproducible local/deployed application
- **Pytest + GitHub Actions** — automated security regression testing
- **Terraform** — AWS reference infrastructure

## 🌐 Live deployment

The application is deployed as a public Render web service from this repository.

After deployment, the useful endpoints are:

```text
/                  → Security dashboard
/health            → Application health
/docs              → FastAPI Swagger documentation
/api/policy        → Active policy configuration
/api/scenarios     → Demonstration traffic scenarios
```

> The live service is a safe demonstration environment. AWS/private-data-center infrastructure is represented through Terraform and policy manifests; production credentials and sensitive infrastructure are not stored here.

## 🏗️ Architecture

```text
                         INTERNET / USERS
                                │
                              WAF / ALB
                                │
                 ┌──────────────┴──────────────┐
                 │          AWS CLOUD           │
                 │                              │
                 │   ┌─────────┐  ┌─────────┐  │
                 │   │Teaching │  │Research │  │
                 │   │   VPC   │  │   VPC   │  │
                 │   └────┬────┘  └────┬────┘  │
                 │        │            │       │
                 │   Security Groups + IAM     │
                 │        └─────┬──────┘       │
                 │              │              │
                 │       Transit Gateway       │
                 │              │              │
                 │        Security / Logs      │
                 └──────────────┼───────────────┘
                                │
                          Site-to-Site VPN
                                │
                    ┌───────────▼───────────┐
                    │   PRIVATE DATA CENTER │
                    └───────────────────────┘

          Kubernetes workloads enforce default-deny
          NetworkPolicies with explicit allow rules.
```

## 🔐 Security model

The central principle is **default deny**:

```text
Request
   ↓
Explicit DENY rule? ── YES ──→ ❌ DENY
   │
   NO
   ↓
Explicit ALLOW rule? ── YES ──→ ✅ ALLOW
   │
   NO
   ↓
❌ DENY — default-deny policy
```

### Demonstration traffic

| Source | Destination | Port | Result |
|---|---|---:|---|
| Internet | Teaching | 443 | ✅ ALLOW |
| Teaching | Database | 5432 | ✅ ALLOW |
| Teaching | DNS | 53 | ✅ ALLOW |
| Teaching | Research | 443 | ❌ DENY |
| Research | Teaching | 443 | ❌ DENY |
| Internet | Database | 5432 | ❌ DENY |
| Developer | Security Admin | 443 | ❌ DENY |

The browser does **not** make these decisions. The frontend calls FastAPI, and the backend policy engine evaluates the request server-side.

## 🖥️ Technology stack

```text
Frontend        HTML5 · CSS3 · JavaScript
Backend         Python · FastAPI
Security        Policy engine · Default deny · Security events
Cloud           AWS VPC · Transit Gateway · Security Groups · IAM
Kubernetes      NetworkPolicy · Namespace isolation
Infrastructure  Terraform
Containers      Docker
Testing         Pytest · GitHub Actions
Deployment      Render
```

## 📁 Repository structure

```text
secure-hybrid-datacenter/
├── working_demo/
│   ├── app/
│   │   ├── main.py
│   │   ├── security.py
│   │   ├── event_service.py
│   │   ├── policy.json
│   │   └── static/
│   ├── tests/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── render.yaml
├── terraform/
├── kubernetes/
├── policies/
├── docs/
├── diagrams/
├── .github/workflows/ci.yml
├── LICENSE
└── README.md
```

## 🚀 Run locally

### Docker

```bash
cd working_demo
docker compose up --build
```

Open `http://localhost:8000`.

### Python

```bash
cd working_demo
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Then:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the dashboard at `http://localhost:8000` and API documentation at `http://localhost:8000/docs`.

## 🧪 Testing & CI

Run locally from `working_demo`:

```bash
pytest -q
python -m compileall app tests
```

GitHub Actions runs the automated tests and Python compilation checks on pushes and pull requests.

**Current status: CI passing ✅**

## ☸️ Kubernetes security

The manifests demonstrate:

1. Namespace isolation.
2. Default-deny ingress/egress.
3. Explicit application-to-database access.
4. Restricted cross-namespace traffic.
5. Controlled DNS resolution.

The same policy philosophy is used throughout the project: **required traffic is explicitly allowed; everything else is denied.**

## ☁️ AWS / Terraform

The Terraform directory provides a reference architecture for:

- VPC segmentation
- Subnets and routing
- Transit Gateway
- Security Groups
- IAM least privilege
- VPC Flow Logs

It is intentionally presented as a reference implementation rather than a claim of production AWS deployment. Review CIDRs, routes, IAM permissions, regions, availability zones and costs before applying it to an AWS account.

## 🧠 Threat model

| Threat | Mitigation |
|---|---|
| Internet → database | Private subnet + restrictive Security Group |
| Teaching → Research lateral movement | Kubernetes NetworkPolicy |
| Workload → private DC movement | Controlled TGW/VPN routing |
| Privilege escalation | IAM least privilege |
| Unknown network flow | Default deny + logging |
| Security regression | Automated tests + CI |

See [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md) and [`docs/SKILLS_MATRIX.md`](docs/SKILLS_MATRIX.md).

## 🎤 Five-minute demo

1. Show the hybrid architecture.
2. Open the deployed security dashboard.
3. Test Internet → Teaching :443 → **ALLOW**.
4. Test Teaching → Database :5432 → **ALLOW**.
5. Test Teaching → Research :443 → **DENY**.
6. Test Internet → Database :5432 → **DENY**.
7. Open `/docs` to demonstrate the FastAPI backend.
8. Show GitHub Actions with the green CI check.
9. Explain default deny, least privilege and defense in depth.

See [`docs/FINAL_DEMO_SCRIPT.md`](docs/FINAL_DEMO_SCRIPT.md).

## ⚠️ Security scope

No production credentials, private keys, passwords, Terraform state or sensitive network information are stored in this repository. The live/local application is a safe proof-of-concept; cloud and private-data-center controls are represented through infrastructure-as-code and policy manifests.

## 👩‍💻 Author

**Siri Lalitha Adapa**

Cybersecurity / Cloud / Data Engineering Project

## 📄 License

MIT License — see [`LICENSE`](LICENSE).
