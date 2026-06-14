#!/bin/bash

set -e

echo "======================================="
echo "KRONOS Deployment Started"
echo "======================================="

echo "[1/5] Initializing Terraform..."
cd terraform
terraform init

echo "[2/5] Applying Infrastructure..."
terraform apply -auto-approve

echo "[3/5] Updating kubeconfig..."
aws eks update-kubeconfig \
  --region ap-south-1 \
  --name kronos

cd ..

echo "[4/5] Validating Kubernetes Cluster..."
kubectl get nodes

echo "[5/5] Deployment Validation..."
kubectl get namespaces
kubectl get pods -A

echo "======================================="
echo "KRONOS Deployment Completed"
echo "======================================="