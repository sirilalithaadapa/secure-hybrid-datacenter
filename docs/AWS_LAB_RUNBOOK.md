# AWS Security Lab Runbook

This runbook turns the project into a real AWS lab without treating the lab as production infrastructure.

## Safety rules

- Never commit AWS access keys, secret keys, session tokens, kubeconfigs, Terraform state, or IdP secrets.
- Prefer AWS IAM Identity Center for human access and short-lived credentials.
- Enable MFA and a billing budget before creating paid resources.
- Run `terraform plan` before every apply.
- Destroy the lab when the demonstration is finished.

## 1. Account bootstrap

1. Sign in to the AWS console with an account-management/admin identity.
2. Choose the lab region (the repository default is `ap-south-1`; change it if needed).
3. Enable IAM Identity Center and connect the organization's IdP if available.
4. Create permission sets for `SecurityAdmin`, `SecurityAnalyst`, `Developer`, and `ReadOnly`.
5. Enable CloudTrail and centralize audit logs.
6. Create an AWS Budgets monthly cost budget with email alerts.
7. Confirm the account has no unexpected running EC2, EKS, NAT Gateway, Network Firewall, VPN, or Transit Gateway resources before starting.

## 2. Local credentials

Use AWS CLI SSO rather than long-lived keys:

```bash
aws configure sso
aws sso login --profile security-lab
aws sts get-caller-identity --profile security-lab
```

Then use the profile with Terraform:

```bash
export AWS_PROFILE=security-lab
```

Windows PowerShell:

```powershell
$env:AWS_PROFILE = "security-lab"
```

## 3. Terraform preflight

```bash
cd terraform
terraform init
terraform fmt -check
terraform validate
terraform plan -var-file=terraform.tfvars
```

Review the plan carefully. Do not apply if the plan contains resources you did not intend to create.

## 4. Hybrid networking

The intended topology is:

```text
EKS/application VPCs
       |
Transit Gateway
       |
VPN attachment
       |
Customer Gateway / on-prem firewall
       |
Private data center
```

The VPN section is intentionally separated from the basic VPC build because a real Site-to-Site VPN requires a customer-gateway endpoint and an on-prem device or software VPN. Do not invent an on-prem public IP.

## 5. EKS

EKS should use private worker subnets across at least two Availability Zones. Cluster and node IAM roles must be separate. Kubernetes NetworkPolicies provide workload-level segmentation in addition to AWS Security Groups.

## 6. Firewall and logging

Network Firewall is an optional paid control. Enable it only for the AWS lab demonstration. Send firewall, VPC Flow Logs, EKS control-plane logs, and CloudTrail events to CloudWatch/S3 as appropriate.

## 7. Validation checklist

- [ ] IAM Identity Center login works
- [ ] MFA is enabled
- [ ] Budget alert exists
- [ ] VPCs and subnets exist in two AZs
- [ ] Route tables match the intended trust boundaries
- [ ] TGW attachments and route tables are correct
- [ ] VPN tunnels are established only when an on-prem endpoint is available
- [ ] EKS nodes are private
- [ ] Default-deny Kubernetes NetworkPolicy is active
- [ ] Network Firewall policy is logging expected decisions
- [ ] Flow Logs and CloudTrail are receiving events
- [ ] Security tests still pass

## 8. Destroy

When the lab is no longer needed:

```bash
terraform destroy -var-file=terraform.tfvars
```

Then verify in the AWS console that paid resources such as NAT Gateways, Network Firewall endpoints, EKS clusters/node groups, VPN connections, and Transit Gateway attachments are gone.

Some billing records can remain visible after deletion because AWS billing/reporting is not instantaneous.
