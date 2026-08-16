resource "aws_flow_log" "app" {
  iam_role_arn    = aws_iam_role.flow_logs.arn
  log_destination = aws_cloudwatch_log_group.vpc_flow.arn
  traffic_type    = "ALL"
  vpc_id          = aws_vpc.app.id
}

resource "aws_cloudwatch_log_group" "vpc_flow" {
  name              = "/hybrid-security/vpc-flow"
  retention_in_days = 30
}

resource "aws_iam_role" "flow_logs" {
  name = "hybrid-security-vpc-flow-logs"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "vpc-flow-logs.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}
