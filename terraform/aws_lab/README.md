# AWS Lab Terraform

This directory is the real AWS lab layer for the project. It is intentionally separate from the existing reference architecture.

## Important

`enable_nat_gateway`, `enable_transit_gateway`, and `enable_eks` default to `false` so a first `terraform plan` does not unexpectedly create high-cost resources.

The lab VPC/subnets/route tables are low-cost networking resources. NAT, TGW, EKS, VPN and Network Firewall should be enabled only for the corresponding demonstration and destroyed afterwards.

## Quick start

```bash
cd terraform/aws_lab
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform fmt -check
terraform validate
terraform plan
```

Use an AWS SSO profile rather than access keys:

```bash
export AWS_PROFILE=security-lab
aws sts get-caller-identity
```

Windows PowerShell:

```powershell
$env:AWS_PROFILE = "security-lab"
aws sts get-caller-identity
```

## Lab stages

### Stage 1 — network foundation

Keep all optional paid services disabled. Apply only after reviewing the plan.

### Stage 2 — NAT/TGW

Set the corresponding flags to `true`, run `terraform plan`, review the charges/resources, then apply.

### Stage 3 — EKS

Enable EKS only after the network foundation is stable. EKS creates a cluster and managed node group and can incur ongoing charges.

### Stage 4 — VPN

Do not enable VPN until a real customer-gateway endpoint and on-prem device/software VPN are available.

### Stage 5 — Network Firewall

Treat Network Firewall as a dedicated lab exercise. It creates hourly endpoint and traffic-processing costs.

## Cleanup

```bash
terraform destroy -var-file=terraform.tfvars
```

Verify in the AWS console that EKS, NAT Gateway, Transit Gateway attachments, VPN, Network Firewall and related resources are gone.
