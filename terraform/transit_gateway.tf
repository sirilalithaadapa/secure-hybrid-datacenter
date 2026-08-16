resource "aws_ec2_transit_gateway" "main" {
  description = "Central hybrid security routing hub"
  default_route_table_association = "disable"
  default_route_table_propagation = "disable"
  tags = { Name = "cisco-hybrid-tgw" }
}
resource "aws_ec2_transit_gateway_vpc_attachment" "app_a" { subnet_ids = [aws_subnet.app_a_private.id], transit_gateway_id = aws_ec2_transit_gateway.main.id, vpc_id = aws_vpc.this["app_a"].id, tags = { Name = "tgw-app-a" } }
resource "aws_ec2_transit_gateway_vpc_attachment" "app_b" { subnet_ids = [aws_subnet.app_b_private.id], transit_gateway_id = aws_ec2_transit_gateway.main.id, vpc_id = aws_vpc.this["app_b"].id, tags = { Name = "tgw-app-b" } }
resource "aws_ec2_transit_gateway_vpc_attachment" "shared" { subnet_ids = [aws_subnet.shared_private.id], transit_gateway_id = aws_ec2_transit_gateway.main.id, vpc_id = aws_vpc.this["shared"].id, tags = { Name = "tgw-shared" } }
resource "aws_ec2_transit_gateway_vpc_attachment" "security" { subnet_ids = [aws_subnet.security_private.id], transit_gateway_id = aws_ec2_transit_gateway.main.id, vpc_id = aws_vpc.this["security"].id, tags = { Name = "tgw-security" } }
resource "aws_ec2_transit_gateway_route_table" "application" { transit_gateway_id = aws_ec2_transit_gateway.main.id, tags = { Name = "tgw-application-isolation" } }
resource "aws_ec2_transit_gateway_route_table_association" "app_a" { transit_gateway_attachment_id = aws_ec2_transit_gateway_vpc_attachment.app_a.id, transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.application.id }
resource "aws_ec2_transit_gateway_route_table_association" "app_b" { transit_gateway_attachment_id = aws_ec2_transit_gateway_vpc_attachment.app_b.id, transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.application.id }
# Production deployments should add explicit routes/propagation only for documented dependencies.
