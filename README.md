# Secure Hybrid Data Center Architecture — Cyber Security Internship

A practical cybersecurity project based on the Cisco Virtual Internship 2026 student problem statement.

## Objective

Design a secure hybrid data-center architecture for a college environment where applications run across private data centers and public cloud, workloads use Kubernetes, users need secure access, and a compromise of one workload must not spread to other applications or the enterprise network.

## Solution

- Hybrid connectivity
- AWS VPC segmentation
- Transit Gateway
- Security Groups
- IAM least privilege
- Kubernetes NetworkPolicies
- Default-deny workload isolation
- Network monitoring / flow logs
- Threat modeling
- Runnable local security-policy demo

## Working demo

The `working_demo/` directory contains a real FastAPI application that enforces the security policy on the server side.

```bash
cd working_demo
docker compose up --build
```

Open `http://localhost:8000`.

Without Docker:

```bash
cd working_demo
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Demo scenarios

| Traffic flow | Result |
|---|---|
| Internet -> Teaching :443 | ALLOW |
| Teaching -> Database :5432 | ALLOW |
| Research -> Database :5432 | ALLOW |
| Teaching -> Research :443 | DENY |
| Research -> Teaching :443 | DENY |
| Internet -> Database | DENY |
| Developer -> Security Admin | DENY |

The browser is not simply displaying hard-coded results: the backend evaluates requests against the policy engine and protected service endpoints enforce the same policy.

## Architecture

```text
INTERNET / USERS
       |
    WAF / ALB
       |
  APPLICATION VPC
    /       \
Teaching   Research
    \       /
   Private Database
       |
 Transit Gateway
       |
 Security / Shared VPCs
       |
 Site-to-Site VPN
       |
 PRIVATE DATA CENTER
```

## Cloud reference implementation

`terraform/` contains the AWS-oriented reference design.

`kubernetes/` contains default-deny and explicit allow-list workload policies.

This project intentionally keeps the cloud infrastructure as a reference implementation so the working demo can be run safely without an AWS bill.

## Documentation

- `docs/ARCHITECTURE.md` — architecture explanation
- `docs/SECURITY_CONTROLS.md` — security control matrix
- `docs/THREAT_MODEL.md` — threat model
- `docs/DEMO.md` — five-minute demo guide
- `docs/PRESENTATION_NOTES.md` — speaking notes
- `diagrams/` — architecture diagrams

## CI

GitHub Actions runs Python tests and compilation checks on pushes and pull requests.

## Security note

Never commit AWS access keys, passwords, private keys, Terraform state files, or other secrets.

> The local application is a proof-of-concept demonstrating the security behavior of the proposed architecture. In production, the same trust boundaries would be enforced using cloud IAM, VPC routing, security groups, network firewalls, Kubernetes NetworkPolicies and centralized logging.
