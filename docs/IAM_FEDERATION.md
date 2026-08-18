# IAM Federation and Least Privilege

## Target design

```text
Corporate IdP (Entra ID / Okta)
          |
       SAML 2.0
          |
IAM Identity Center
          |
   Permission Sets
   |       |       |
Security  Analyst  ReadOnly
Admin
          |
      AWS account
```

Human users should use federated, short-lived sessions rather than long-lived IAM access keys.

## Permission-set model

- `SecurityAdmin`: security configuration and incident-response administration.
- `SecurityAnalyst`: read security telemetry and investigate findings.
- `Developer`: application deployment permissions without unrestricted security administration.
- `ReadOnly`: read-only access for review and demos.

## Lab setup

1. Enable IAM Identity Center.
2. Add the external identity source or use the built-in directory for the lab.
3. Create groups matching the permission sets.
4. Assign users/groups to the AWS lab account.
5. Require MFA through the identity provider.
6. Test each role with `aws sso login` and `aws sts get-caller-identity`.

Do not put federation secrets, SAML certificates, SCIM tokens, or identity-provider credentials in this repository.
