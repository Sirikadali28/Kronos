**# Terraform Infrastructure**



**This directory contains the Terraform configuration used to provision the AWS infrastructure for the KRONOS project.**



**## Components**



**- Amazon EKS Cluster**

**- Managed Node Group**

**- VPC and Subnets**

**- IAM Roles for Service Accounts (IRSA)**



**## Deployment**



**Initialize Terraform:**



**terraform init**



**Review the execution plan:**



**terraform plan**



**Apply the infrastructure:**



**terraform apply**



**Update kubeconfig:**



**aws eks update-kubeconfig \\**

&#x20; **--region ap-south-1 \\**

&#x20; **--name kronos**

