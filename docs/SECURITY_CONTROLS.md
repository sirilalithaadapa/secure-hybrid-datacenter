# Security Controls Matrix

| Control | Implementation | Purpose |
|---|---|---|
| Identity | Federated IAM + roles + MFA | Prevent uncontrolled access |
| Least privilege | Scoped IAM policies | Reduce blast radius |
| Network hub | Transit Gateway | Centralize hybrid routing |
| Hybrid encryption | Site-to-Site VPN | Protect on-prem/cloud traffic |
| VPC isolation | Separate application VPCs | Stop lateral movement |
| Route isolation | TGW route tables | Control network communication |
| Ingress protection | WAF + ALB | Reduce public attack surface |
| Stateful filtering | Security Groups | Resource-level traffic control |
| Kubernetes isolation | Namespaces | Application separation |
| Kubernetes filtering | NetworkPolicies | East-west traffic control |
| Workload identity | IAM roles | Avoid embedded cloud credentials |
| Central inspection | Network Firewall | Inspect suspicious traffic |
| Network telemetry | Flow Logs | Investigate traffic patterns |
| Audit | CloudTrail/CloudWatch | Track administration |
| Encryption | TLS + encryption at rest | Protect sensitive data |
| Incident response | Isolation/revoke/rotate | Contain compromise |

## Core rule

The system starts with default deny and adds only documented business-required flows.
