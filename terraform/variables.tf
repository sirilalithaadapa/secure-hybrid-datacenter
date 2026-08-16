variable "aws_region" { type = string, description = "AWS region for the reference deployment.", default = "ap-south-1" }
variable "environment" { type = string, default = "lab" }
variable "onprem_cidr" { type = string, default = "10.10.0.0/16" }
variable "app_a_cidr" { type = string, default = "10.20.0.0/16" }
variable "app_b_cidr" { type = string, default = "10.30.0.0/16" }
variable "shared_cidr" { type = string, default = "10.40.0.0/16" }
variable "security_cidr" { type = string, default = "10.50.0.0/16" }
