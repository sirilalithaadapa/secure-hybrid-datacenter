locals { vpcs = { app_a = var.app_a_cidr, app_b = var.app_b_cidr, shared = var.shared_cidr, security = var.security_cidr } }
resource "aws_vpc" "this" {
  for_each = local.vpcs
  cidr_block = each.value
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = { Name = "cisco-${each.key}-vpc", Zone = each.key }
}
resource "aws_subnet" "app_a_private" { vpc_id = aws_vpc.this["app_a"].id, cidr_block = "10.20.10.0/24", availability_zone = "${var.aws_region}a", tags = { Name = "app-a-private-a", Tier = "application" } }
resource "aws_subnet" "app_a_data" { vpc_id = aws_vpc.this["app_a"].id, cidr_block = "10.20.20.0/24", availability_zone = "${var.aws_region}a", tags = { Name = "app-a-data-a", Tier = "data" } }
resource "aws_subnet" "app_b_private" { vpc_id = aws_vpc.this["app_b"].id, cidr_block = "10.30.10.0/24", availability_zone = "${var.aws_region}a", tags = { Name = "app-b-private-a", Tier = "application" } }
resource "aws_subnet" "shared_private" { vpc_id = aws_vpc.this["shared"].id, cidr_block = "10.40.10.0/24", availability_zone = "${var.aws_region}a", tags = { Name = "shared-private-a", Tier = "shared-services" } }
resource "aws_subnet" "security_private" { vpc_id = aws_vpc.this["security"].id, cidr_block = "10.50.10.0/24", availability_zone = "${var.aws_region}a", tags = { Name = "security-private-a", Tier = "inspection" } }
resource "aws_route_table" "private" { for_each = local.vpcs, vpc_id = aws_vpc.this[each.key].id, tags = { Name = "cisco-${each.key}-private-rt" } }
