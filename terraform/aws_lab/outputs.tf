output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}

output "transit_gateway_id" {
  value = var.enable_transit_gateway ? aws_ec2_transit_gateway.this[0].id : null
}

output "eks_cluster_name" {
  value = var.enable_eks ? aws_eks_cluster.this[0].name : null
}
