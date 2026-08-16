# Security Skills Demonstrated

| Skill | Evidence in repository | What it demonstrates |
|---|---|---|
| Hybrid connectivity | `terraform/`, architecture diagram | Controlled cloud-to-private-DC connectivity concept |
| AWS VPC segmentation | Terraform VPC/subnet/security-group definitions | Trust-boundary design |
| Transit Gateway | `terraform/transit_gateway.tf` | Centralized hub routing model |
| Security Groups | `terraform/security_groups.tf` | Least-privilege network access |
| IAM least privilege | `policies/`, `terraform/iam.tf` | Identity-based authorization |
| Kubernetes NetworkPolicy | `kubernetes/` | East-west workload isolation |
| Default deny | `working_demo/app/security.py`, Kubernetes manifests | Secure-by-default enforcement |
| Flow logs | `terraform/flow_logs.tf` | Network visibility and investigation |
| Threat modeling | `docs/THREAT_MODEL.md` | Risk-to-control mapping |
| Python / FastAPI | `working_demo/app/` | Backend API and policy enforcement |
| HTML/CSS/JavaScript | `working_demo/app/static/` | Security operations dashboard |
| Docker | `working_demo/Dockerfile`, `docker-compose.yml` | Reproducible deployment |
| Automated testing | `working_demo/tests/`, `.github/workflows/ci.yml` | Security regression testing |
| GitHub | Repository + CI workflow | Version control and engineering workflow |
