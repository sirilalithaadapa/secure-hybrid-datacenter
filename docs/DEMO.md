# Five-minute Demo

1. Open the working demo dashboard.
2. Explain the architecture: users -> WAF/ALB -> application zones -> Transit Gateway -> security/shared services -> private data center.
3. Run `internet -> teaching :443` and show ALLOW.
4. Run `teaching -> database :5432` and show ALLOW.
5. Simulate compromise by running `teaching -> research :443` and show DENY.
6. Run `internet -> database` and show DENY.
7. Explain that default-deny, IAM, VPC segmentation, Security Groups and Kubernetes NetworkPolicies work together to reduce blast radius.
8. Explain that the local FastAPI app is a proof-of-concept for the policy behavior, while Terraform/Kubernetes files map the design to production controls.
