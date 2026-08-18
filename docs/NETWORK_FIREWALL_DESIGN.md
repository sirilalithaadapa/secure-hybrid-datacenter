# AWS Network Firewall Design

Network Firewall is a separate paid lab stage. It should sit at a deliberate inspection boundary rather than being added without corresponding route-table changes.

## Target path

```text
Private application subnet
        |
   inspection route
        |
Network Firewall endpoints
        |
   egress route
        |
 NAT Gateway / IGW
```

For north-south and east-west inspection, route tables must be designed around the firewall endpoint ENIs. The firewall subnet must be dedicated and should not host application workloads.

## Security policy model

Start with an explicit, small policy:

- allow only required DNS/HTTPS egress;
- deny known unwanted destinations;
- log stateful decisions;
- expand rules only when the traffic requirement is understood.

Do not use `0.0.0.0/0` allow rules as a substitute for an actual security policy.

## Lab validation

1. Confirm firewall endpoints exist in the intended AZs.
2. Confirm application subnet route tables point inspection traffic to the firewall endpoint.
3. Confirm the post-inspection route reaches NAT/IGW only where intended.
4. Generate a known-good HTTPS/DNS request.
5. Generate a deliberately blocked request.
6. Confirm the event appears in firewall logs.

## Cost warning

Network Firewall endpoints and processed traffic are billable. Enable this stage only for the demonstration and destroy it afterwards.
