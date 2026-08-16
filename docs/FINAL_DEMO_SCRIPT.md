# Final 5-Minute Demo Script

## 1. Problem (30 seconds)

The college has applications across a private data center and public cloud. Faculty and students need secure access, Kubernetes workloads require isolation, and a compromise of one application must not spread to other applications or the enterprise network.

## 2. Architecture (60 seconds)

Show `diagrams/hybrid_architecture.svg`.

Explain: Internet users enter through WAF/ALB. Applications run in isolated cloud zones. Transit Gateway provides controlled routing to security/shared services and the private data center. IAM, Security Groups, Kubernetes NetworkPolicies, firewall inspection and flow logs provide defense in depth.

## 3. Live policy test (90 seconds)

Open the working demo.

Run:
- Internet -> Teaching :443 => ALLOW
- Teaching -> Database :5432 => ALLOW
- Teaching -> Research :443 => DENY
- Internet -> Database => DENY
- Developer -> Security Admin => DENY

Key statement: "The browser is not hard-coded; the FastAPI backend evaluates the request against the policy engine."

## 4. Compromise containment (60 seconds)

Pretend Teaching is compromised. Attempt Teaching -> Research and Teaching -> Private DC. Explain that default-deny workload isolation and network segmentation prevent lateral movement unless an explicit dependency is permitted.

## 5. Close (40 seconds)

The design balances simplicity, security and scale by separating trust boundaries, keeping sensitive services private, using least privilege, and centralizing network visibility. The repository contains the working demo, Kubernetes policies, Terraform reference implementation, tests and documentation.
