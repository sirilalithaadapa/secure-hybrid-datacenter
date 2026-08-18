# AWS Cost Control

This lab intentionally includes services that can incur charges. Treat the AWS environment as temporary.

## Highest-priority cost risks

| Service | Why it can cost money | Lab guidance |
|---|---|---|
| EKS | Cluster hourly charge plus nodes/storage/logging | Create only for the demo; destroy afterwards |
| NAT Gateway | Hourly + data processing | Use only when needed; destroy after lab |
| Transit Gateway | Attachment hourly + data processing | Keep attachments minimal |
| Network Firewall | Endpoint hourly + traffic processing | Enable only for the firewall demonstration |
| Site-to-Site VPN | Connection hourly + data transfer | Create only with a real customer gateway |
| CloudWatch | Ingestion/storage | Use short retention for lab logs |
| EC2/EBS | Instance and storage charges | Use small lab instances and delete them |
| Public IPv4 | Hourly public IPv4 charges | Avoid unnecessary public addresses |

## Before apply

1. Create an AWS Budget with an email alert.
2. Confirm the selected region.
3. Run `terraform plan` and inspect every resource.
4. Record the expected resources and count.
5. Do not apply an unknown plan.

## After the demo

Run:

```bash
terraform destroy -var-file=terraform.tfvars
```

Then manually verify that no paid resources remain.

## Recommended lab discipline

Use one dedicated AWS account for the lab if possible. Never attach the lab to production VPCs, production TGWs, production VPNs, or production EKS clusters.
