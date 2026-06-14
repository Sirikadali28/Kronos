# Cleanup Guide - KRONOS

This guide provides step-by-step instructions for safely tearing down KRONOS resources to avoid unexpected AWS charges.

**⚠️ WARNING**: These commands will DELETE resources. Double-check before executing!

## Cleanup Sequence

Always follow this order to avoid orphaned resources:

1. Delete Kubernetes resources
2. Delete EKS cluster
3. Delete S3 buckets
4. Verify cleanup

## Step 1: Delete Kubernetes Resources (2 minutes)

### Delete Applications

```bash
# Delete all applications in ArgoCD
argocd app list
argocd app delete <app-name>  # Repeat for each app

# Or delete all at once
kubectl delete all --all -A
```

### Delete Namespaces (except system namespaces)

```bash
# Delete custom namespaces
kubectl delete namespace argocd
kubectl delete namespace monitoring
kubectl delete namespace default  # Only if custom resources added

# Keep system namespaces:
# - kube-system
# - kube-public
# - kube-node-lease
```

### Delete PersistentVolumeClaims (PVCs)

```bash
# Check for PVCs
kubectl get pvc -A

# Delete PVCs
kubectl delete pvc <pvc-name> -n <namespace>

# Or delete all
kubectl delete pvc --all -A
```

### Verify Kubernetes Cleanup

```bash
# Check remaining resources
kubectl get all -A

# Should only see kube-system resources
```

## Step 2: Delete EKS Cluster (10-15 minutes)

### Warning: This will delete everything!

```bash
# Create backup (optional but recommended)
kubectl get all -A > cluster-backup.yaml
aws s3 cp cluster-backup.yaml s3://your-bucket/backups/

# Delete cluster
eksctl delete cluster --name kronos --region ap-south-1
```

### What this deletes:
- EKS cluster
- EC2 worker nodes
- Load Balancers (if any)
- VPC resources (if created by eksctl)
- Security groups (if created by eksctl)
- IAM roles and policies

### Monitor deletion progress

```bash
# Check cluster status
aws eks describe-cluster --name kronos --region ap-south-1 2>&1 | grep -i "status"

# Expected: Cluster not found (after deletion complete)
```

## Step 3: Delete S3 Buckets

### List S3 Buckets

```bash
aws s3 ls | grep kronos
```

### Delete Bucket (WARNING: irreversible!)

```bash
# Empty bucket first (required)
aws s3 rm s3://kronos-anomaly-data-${AWS_ACCOUNT_ID} --recursive

# Delete bucket
aws s3 rb s3://kronos-anomaly-data-${AWS_ACCOUNT_ID}

# Verify deletion
aws s3 ls | grep kronos
```

### Backup Before Deletion (Recommended)

```bash
# Download all data
aws s3 sync s3://kronos-anomaly-data-${AWS_ACCOUNT_ID} ./kronos-backup-$(date +%Y%m%d)

# Then proceed with deletion
aws s3 rm s3://kronos-anomaly-data-${AWS_ACCOUNT_ID} --recursive
aws s3 rb s3://kronos-anomaly-data-${AWS_ACCOUNT_ID}
```

## Step 4: Cleanup CloudFormation Stacks

eksctl creates CloudFormation stacks automatically:

```bash
# List all stacks
aws cloudformation list-stacks --region ap-south-1 --query 'StackSummaries[*].StackName'

# Delete eksctl-created stacks
aws cloudformation delete-stack --stack-name eksctl-kronos-nodegroup-ng-xxxxx --region ap-south-1
aws cloudformation delete-stack --stack-name eksctl-kronos-cluster --region ap-south-1

# Check deletion status
aws cloudformation list-stacks --region ap-south-1 --stack-status-filter DELETE_COMPLETE
```

## Step 5: Cleanup IAM Resources

### Delete Custom IAM Roles (if created)

```bash
# List attached policies
aws iam list-attached-role-policies --role-name kronos-service-role

# Detach policies
aws iam detach-role-policy \
  --role-name kronos-service-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSFullAccess

# Delete role
aws iam delete-role --role-name kronos-service-role
```

## Step 6: Verify Complete Cleanup

### Verify No Instances Running

```bash
# List EC2 instances
aws ec2 describe-instances --region ap-south-1 \
  --query 'Reservations[*].Instances[*].[InstanceId,State.Name,Tags[?Key==`Name`].Value|[0]]'

# Should show no kronos-related instances
```

### Verify Cluster Deleted

```bash
# Should error with cluster not found
aws eks describe-cluster --name kronos --region ap-south-1 2>&1
# Expected: ResourceNotFoundException
```

### Verify S3 Buckets Deleted

```bash
aws s3 ls | grep kronos
# Should show no results
```

### Verify VPC Cleanup

```bash
# Check for unattached network interfaces
aws ec2 describe-network-interfaces --region ap-south-1 \
  --filters "Name=status,Values=available"

# Delete unattached interfaces if kronos-related
aws ec2 delete-network-interface --network-interface-id eni-xxxxx
```

## Cost Estimation

### What You'll Be Charged For

If you don't clean up, costs accrue as:

| Resource | Cost/Hour | Cost/Month (24/7) |
|----------|-----------|-------------------|
| 2× t3.medium EC2 | ~$0.14 | ~$103 |
| EKS Control Plane | ~$0.10 | ~$73 |
| EBS Storage (40GB) | ~$0.004 | ~$2.92 |
| Data Transfer | Variable | ~$10-20 |
| **Total** | ~$0.24 | ~$190 |

### Cost Savings from Cleanup

- **Stop after 1 hour**: $0.24
- **Stop after 1 week**: $40
- **Stop after 1 month**: $190+

## Cleanup Checklist

- [ ] Deleted all custom Kubernetes resources
- [ ] Deleted ArgoCD namespace
- [ ] Deleted monitoring namespace
- [ ] Deleted all PVCs and PVs
- [ ] Verified no remaining pods in namespaces
- [ ] Deleted EKS cluster with eksctl
- [ ] Verified cluster no longer exists in AWS console
- [ ] Emptied and deleted S3 buckets
- [ ] Verified S3 bucket deletion in AWS console
- [ ] Deleted all CloudFormation stacks
- [ ] Verified no EC2 instances running
- [ ] Checked final AWS bill (wait 24-48 hours for full update)

## Partial Cleanup (Keep Some Resources)

If you want to keep some components:

### Keep Cluster, Delete Monitoring

```bash
kubectl delete namespace monitoring
helm uninstall monitoring -n monitoring
```

### Keep S3, Delete Everything Else

```bash
# Keep S3 bucket, delete data
aws s3 rm s3://kronos-anomaly-data-${AWS_ACCOUNT_ID} --recursive --exclude "reports/*"

# Or keep bucket, delete cluster
eksctl delete cluster --name kronos --region ap-south-1
```

### Keep Cluster Running but Stop Nodes

```bash
# Scale down nodes to 0
eks scale nodegroup --cluster=kronos --nodes=0

# Restart later
eks scale nodegroup --cluster=kronos --nodes=2
```

## Troubleshooting Cleanup

### Cluster Deletion Stuck

```bash
# Force delete (use with caution)
eksctl delete cluster --name kronos --region ap-south-1 --force

# Or manually delete CloudFormation stack
aws cloudformation delete-stack --stack-name eksctl-kronos-cluster --region ap-south-1
```

### S3 Bucket Not Deleting

```bash
# Check for versioning
aws s3api get-bucket-versioning --bucket kronos-anomaly-data-${AWS_ACCOUNT_ID}

# If versioning enabled, delete all versions
aws s3api delete-object-versions \
  --bucket kronos-anomaly-data-${AWS_ACCOUNT_ID} \
  --key-pattern "*"

# Then delete bucket
aws s3 rb s3://kronos-anomaly-data-${AWS_ACCOUNT_ID} --force
```

### Orphaned Resources

```bash
# Find resources with specific tag
aws ec2 describe-instances --region ap-south-1 \
  --filters "Name=tag:kubernetes.io/cluster/kronos,Values=owned"

# Delete if necessary
aws ec2 terminate-instances --instance-ids <instance-id> --region ap-south-1
```

## Preserve Logs Before Deletion

```bash
# Export kubectl events
kubectl get events -A > events-backup.log

# Export resource definitions
kubectl get all -A -o yaml > resources-backup.yaml

# Export Prometheus data
kubectl exec -n monitoring prometheus-xxx -- tar czf - /prometheus | tar xzf - -C ./prometheus-backup

# Backup to S3
aws s3 cp events-backup.log s3://backup-bucket/kronos-logs/
aws s3 cp resources-backup.yaml s3://backup-bucket/kronos-logs/
```

## Restarting After Cleanup

To redeploy from scratch:

1. Follow [Complete Setup Guide](setup-guide.md)
2. Use backed-up YAML files to quickly recreate resources:
   ```bash
   kubectl apply -f resources-backup.yaml
   ```

## Documentation & Audit Trail

Keep records of:

1. Deletion date and time
2. What was deleted
3. Backup locations
4. Final cost verification
5. Any issues encountered

### Example Cleanup Log

```
=== KRONOS Cleanup Log ===
Date: 2024-06-12
Time: 10:45 UTC
Region: ap-south-1

[10:45] Deleted ArgoCD namespace - 5 pods removed
[10:46] Deleted monitoring namespace - 12 pods removed
[10:47] Deleted all PVCs - 3 volumes removed
[10:48] Starting cluster deletion...
[10:52] EKS cluster eksctl-kronos-nodegroup-ng-xxxxx deleted
[10:55] EKS control plane deleted
[10:56] S3 bucket emptied (150GB)
[10:57] S3 bucket kronos-anomaly-data deleted
[10:58] Cleanup completed successfully

Final Status:
- Cluster: DELETED
- Nodes: TERMINATED
- S3 Bucket: DELETED
- Data Backed Up: YES (s3://backup-bucket/kronos-logs/)
```

## Support

If you encounter issues during cleanup:

1. Check AWS CloudFormation console for failed deletions
2. Check EC2 console for orphaned instances
3. Check S3 console for buckets stuck in deletion
4. Search AWS documentation for specific error messages
5. Contact AWS Support if critical resources are stuck

---

**Previous**: [Complete Setup Guide](setup-guide.md)  
**Next**: Consider [Lessons Learned](lessons-learned.md) for insights from this project
