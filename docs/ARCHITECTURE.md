# Secure Hybrid Data Center Architecture

## Design goal

Support public-cloud and private-data-center applications while preventing a compromise in one workload from becoming unrestricted lateral movement.

## Logical architecture

```text
Internet / Users
       |
    WAF / ALB
       |
 Application VPC
   /        \
Teaching   Research
   \        /
   Private Database
       |
 Transit Gateway
       |
 Security / Shared VPCs
       |
 Site-to-Site VPN
       |
 Private Data Center
```

## Trust boundaries

1. Public ingress boundary — WAF/ALB is the only public application entry point.
2. Application boundary — application workloads run in isolated VPCs/namespaces.
3. Data boundary — databases are private and accept only explicit application traffic.
4. Security boundary — firewall, logging and security administration are isolated.
5. Enterprise boundary — the private data center connects through controlled hybrid routing.

## Security principles

- Default deny
- Least privilege
- Explicit allow lists
- Defense in depth
- Workload identity instead of embedded credentials
- Centralized visibility
- Containment over perimeter-only security

## Scalability

A new application should receive the same template: dedicated trust boundary, IAM role, security group, namespace, default-deny policy, and documented routes/dependencies.
