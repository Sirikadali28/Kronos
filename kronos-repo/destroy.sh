#!/bin/bash

set -e

echo "======================================="
echo "KRONOS Cleanup Started"
echo "======================================="

read -p "Are you sure you want to destroy KRONOS infrastructure? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Cleanup cancelled."
    exit 0
fi

cd terraform

echo "Destroying AWS infrastructure..."
terraform destroy -auto-approve

cd ..

echo "======================================="
echo "KRONOS Cleanup Completed"
echo "======================================="