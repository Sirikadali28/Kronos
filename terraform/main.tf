module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.31"

  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version

  vpc_id = "vpc-0e00ba3980644825e"

  subnet_ids = [
    "subnet-0204cc39bc52662ed",
    "subnet-05ed29d7bc7738998",
    "subnet-0821d70a76847a1ee"
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
