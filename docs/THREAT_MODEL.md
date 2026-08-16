# Threat Model

## T1 — Public application compromise
Controls: WAF, ALB, private application nodes, least-privilege runtime IAM, NetworkPolicies, egress restrictions and flow logging.

## T2 — Lateral movement
Controls: separate VPCs, TGW route-table isolation, security groups, Network ACLs and Kubernetes namespace isolation.

## T3 — Credential theft
Controls: federation, MFA, short-lived sessions, role separation, least privilege and audit logging.

## T4 — Compromised Kubernetes pod
Controls: default-deny NetworkPolicy, namespace separation, service-account/RBAC restrictions and pod security controls.

## T5 — Data exfiltration
Controls: controlled egress, centralized inspection, DNS controls where appropriate, flow logs and runtime identity restrictions.

## T6 — On-premises compromise
Controls: VPN boundary, TGW route tables, security groups, application allow-listing and inspection/logging.

## Core principle

The architecture assumes compromise can happen. The goal is to make compromise contained, observable and recoverable rather than assuming the perimeter will prevent every breach.
