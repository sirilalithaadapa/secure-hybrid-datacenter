# VPN and Transit Gateway Design

## Target topology

```text
Private Data Center
      |
Customer Gateway / Firewall
      |
AWS Site-to-Site VPN
      |
Transit Gateway
  /       |       \
App VPC  Shared   Security
         VPC      VPC
```

## Routing intent

- Application VPCs advertise only required prefixes to the Transit Gateway.
- The VPN attachment receives only the private CIDRs required by the lab.
- Security/shared services are reachable only through explicit TGW route-table associations and propagations.
- Internet traffic is not automatically routed through the VPN.

## VPN prerequisite

A real Site-to-Site VPN requires:

- an AWS customer-gateway configuration;
- the public IP of the customer/on-prem VPN endpoint;
- the on-prem ASN/device configuration;
- matching IKE/IPsec parameters.

Do not enter placeholder values into a production account. For a safe lab, use a real software VPN endpoint only when you understand its networking and lifecycle.

## Validation

```bash
aws ec2 describe-transit-gateway-attachments
aws ec2 search-transit-gateway-routes \
  --transit-gateway-route-table-id <route-table-id> \
  --filters Name=state,Values=active

aws ec2 describe-vpn-connections
```

The final design should demonstrate intentional route propagation rather than a flat all-to-all network.
