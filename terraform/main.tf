module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 21.0"

  name               = var.cluster_name
  kubernetes_version = var.cluster_version

  vpc_id = "vpc-0e00ba3980644825e"

  subnet_ids = [
    "subnet-05ed29d7bc7738998",
    "subnet-0821d70a76847a1ee",
    "subnet-0204cc39bc52662ed"
  ]

  enable_irsa = true

  eks_managed_node_groups = {
    kronos_nodes = {
      instance_types = [var.instance_type]

      min_size     = var.min_size
      max_size     = var.max_size
      desired_size = var.desired_size
    }
  }

  tags = {
    Project     = "Kronos"
    Environment = "Learning"
    ManagedBy   = "Terraform"
  }
}
