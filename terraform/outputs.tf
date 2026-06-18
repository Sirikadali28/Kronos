output "cluster_name" {
  value = module.eks.cluster_name
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "cluster_version" {
  value = module.eks.cluster_version
}

output "region" {
  value = var.aws_region
}
output "ecr_repository_url" {
  value = aws_ecr_repository.kronos_anomaly.repository_url
}
