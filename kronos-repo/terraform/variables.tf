variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "ap-south-1"
}

variable "cluster_name" {
  description = "EKS Cluster Name"
  type        = string
  default     = "kronos"
}

variable "cluster_version" {
  description = "Kubernetes Version"
  type        = string
  default     = "1.34"
}

variable "instance_type" {
  description = "Worker Node Instance Type"
  type        = string
  default     = "t3.small"
}

variable "desired_size" {
  type    = number
  default = 2
}

variable "min_size" {
  type    = number
  default = 1
}

variable "max_size" {
  type    = number
  default = 2
}