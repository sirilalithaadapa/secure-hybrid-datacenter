variable "aws_region" {
  type        = string
  description = "AWS region for the lab."
  default     = "ap-south-1"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR for the isolated lab VPC."
  default     = "10.60.0.0/16"
}

variable "availability_zones" {
  type        = list(string)
  description = "Two AZs used for the lab."
  default     = ["ap-south-1a", "ap-south-1b"]
}

variable "public_subnet_cidrs" {
  type        = list(string)
  default     = ["10.60.1.0/24", "10.60.2.0/24"]
}

variable "private_subnet_cidrs" {
  type        = list(string)
  default     = ["10.60.11.0/24", "10.60.12.0/24"]
}

variable "enable_nat_gateway" {
  type        = bool
  description = "Creates one NAT Gateway per AZ. Paid resource."
  default     = false
}

variable "enable_transit_gateway" {
  type        = bool
  description = "Creates a Transit Gateway and VPC attachment. Paid resource."
  default     = false
}

variable "enable_eks" {
  type        = bool
  description = "Creates an EKS control plane and managed node group. Paid resources."
  default     = false
}

variable "eks_instance_type" {
  type        = string
  description = "Small EC2 instance type for the EKS lab node group."
  default     = "t3.small"
}

variable "enable_flow_logs" {
  type        = bool
  description = "Enable VPC Flow Logs to an existing CloudWatch Logs destination."
  default     = false
}

variable "flow_log_destination_arn" {
  type        = string
  description = "Existing CloudWatch Logs log group ARN for VPC Flow Logs."
  default     = ""
}

variable "flow_log_iam_role_arn" {
  type        = string
  description = "IAM role ARN allowing VPC Flow Logs to publish to CloudWatch Logs."
  default     = ""
}
