resource "aws_ecr_repository" "kronos_anomaly" {
  name                 = "kronos-anomaly"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project     = "Kronos"
    Environment = "Learning"
    ManagedBy   = "Terraform"
  }
}
