resource "aws_security_group" "alb" {
  name = "cisco-sg-alb"
  description = "Public application load balancer"
  vpc_id = aws_vpc.this["app_a"].id
  ingress { description = "HTTPS from Internet", protocol = "tcp", from_port = 443, to_port = 443, cidr_blocks = ["0.0.0.0/0"] }
  egress { description = "Application traffic", protocol = "tcp", from_port = 443, to_port = 443, security_groups = [aws_security_group.app.id] }
}
resource "aws_security_group" "app" {
  name = "cisco-sg-app"
  description = "Private application tier"
  vpc_id = aws_vpc.this["app_a"].id
  ingress { description = "Only from ALB", protocol = "tcp", from_port = 443, to_port = 443, security_groups = [aws_security_group.alb.id] }
  egress { description = "HTTPS for approved dependencies", protocol = "tcp", from_port = 443, to_port = 443, cidr_blocks = ["10.0.0.0/8"] }
}
resource "aws_security_group" "db" {
  name = "cisco-sg-db"
  description = "Private database tier"
  vpc_id = aws_vpc.this["app_a"].id
  ingress { description = "PostgreSQL only from application tier", protocol = "tcp", from_port = 5432, to_port = 5432, security_groups = [aws_security_group.app.id] }
}
