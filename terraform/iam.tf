data "aws_iam_policy_document" "developer" {
  statement { sid = "ReadApplicationLogs", effect = "Allow", actions = ["logs:GetLogEvents", "logs:FilterLogEvents", "logs:DescribeLogStreams", "logs:DescribeLogGroups"], resources = ["*"] }
  statement { sid = "ReadEKS", effect = "Allow", actions = ["eks:DescribeCluster", "eks:ListClusters"], resources = ["*"] }
}
resource "aws_iam_role" "developer" {
  name = "CiscoDeveloperRole"
  assume_role_policy = jsonencode({Version="2012-10-17",Statement=[{Effect="Allow",Principal={AWS="arn:aws:iam::123456789012:root"},Action="sts:AssumeRole",Condition={Bool={"aws:MultiFactorAuthPresent"="true"}}}]})
}
resource "aws_iam_role_policy" "developer" { role = aws_iam_role.developer.id, policy = data.aws_iam_policy_document.developer.json }
# Replace the example trust relationship with the organization's federation/IdP trust before production.
