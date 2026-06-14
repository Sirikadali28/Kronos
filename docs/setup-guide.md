# Complete Setup Guide - KRONOS

This guide walks through the entire KRONOS implementation from scratch.

**Estimated Time**: 1-2 hours
**Cost**: ~$0.50-1.00/hour on AWS (t3.medium instances)
**Complexity**: Intermediate

## Prerequisites

### Required Software

Install these tools on your local machine:

1. **AWS CLI 2.13+**
   ```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   ```

2. **eksctl 0.162+**
   ```bash
   curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
   sudo mv /tmp/eksctl /usr/local/bin
   ```

3. **kubectl 1.28+**
   ```bash
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.1/2023-09-14/bin/linux/amd64/kubectl
   chmod +x ./kubectl
   sudo mv ./kubectl /usr/local/bin
   ```

4. **Helm 3.12+**
   ```bash
   curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
   ```

5. **Python 3.9+**
   ```bash
   # Check version
   python3 --version
   
   # Install pip packages
   pip install pandas numpy
   ```

### AWS Account Setup

1. Create AWS account with billing enabled
2. Create IAM user with permissions:
   - `AmazonEC2FullAccess`
   - `AmazonEKSFullAccess`
   - `IAMFullAccess`
   - `AmazonS3FullAccess`

3. Configure AWS credentials:
   ```bash
   aws configure
   # Enter: Access Key ID, Secret Access Key, Region (ap-south-1), Format (json)
   ```

4. Verify configuration:
   ```bash
   aws sts get-caller-identity
   ```

## Step 1: Create EKS Cluster (20 minutes)

### 1.1 Create Cluster

```bash
eksctl create cluster \
  --name kronos \
  --region ap-south-1 \
  --nodes 2 \
  --node-type t3.medium \
  --node-volume-size 20 \
  --managed
```

### 1.2 Verify Cluster

```bash
# Check cluster info
kubectl cluster-info

# List nodes
kubectl get nodes

# Check system pods
kubectl get pods -A
```

**Expected Output:**
```
NAME                            STATUS   ROLES    AGE
ip-192-168-x-xx.ec2.internal   Ready    <none>   5m
ip-192-168-x-yy.ec2.internal   Ready    <none>   5m
```

### 1.3 Create S3 Bucket for Anomaly Data

```bash
# Create bucket (bucket names must be globally unique)
aws s3 mb s3://kronos-anomaly-data-${AWS_ACCOUNT_ID} --region ap-south-1

# Verify
aws s3 ls | grep kronos
```

## Step 2: Deploy ArgoCD (10 minutes)

See [ArgoCD Installation Guide](../argocd/installation.md)

```bash
# Create namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Get initial password
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d

# Port forward
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Access at: https://localhost:8080
```

## Step 3: Deploy Monitoring Stack (15 minutes)

See [Prometheus Installation Guide](../monitoring/prometheus-installation.md)

```bash
# Create namespace
kubectl create namespace monitoring

# Add Helm repo
helm repo add prometheus-community \
  https://prometheus-community.github.io/helm-charts
helm repo update

# Install stack
helm install monitoring \
  prometheus-community/kube-prometheus-stack \
  -n monitoring \
  --set prometheus.prometheusSpec.retention=30d \
  --set grafana.adminPassword=admin

# Verify
kubectl get pods -n monitoring
```

### Access Monitoring Dashboards

```bash
# Prometheus (metrics)
kubectl port-forward -n monitoring svc/prometheus-operated 9090:9090
# Visit: http://localhost:9090

# Grafana (visualization)
kubectl port-forward -n monitoring svc/grafana 3000:80
# Visit: http://localhost:3000 (admin/admin)
```

## Step 4: Run Anomaly Detection Pipeline (5 minutes)

See [Anomaly Detection Guide](../anomaly-detection/README.md)

```bash
# Navigate to anomaly detection directory
cd anomaly-detection

# Install dependencies
pip install -r requirements.txt

# Run detection
python detect_anomalies.py

# Check results
cat anomaly-report.csv

# Upload to S3 (optional)
aws s3 cp anomaly-report.csv s3://kronos-anomaly-data-${AWS_ACCOUNT_ID}/reports/
```

## Step 5: Verification Checklist

- [ ] EKS cluster running with 2 nodes in Ready state
- [ ] All kube-system pods running (coredns, kube-proxy, etc.)
- [ ] ArgoCD pods running in argocd namespace
- [ ] ArgoCD web UI accessible and login successful
- [ ] Prometheus metrics being collected (targets showing "UP")
- [ ] Grafana dashboard accessible with data
- [ ] S3 bucket created and accessible
- [ ] Anomaly detection pipeline executed successfully
- [ ] anomaly-report.csv generated with results

## Accessing Components

### Local Access (Port Forwarding)

All components are internal by default. Access them with:

```bash
# ArgoCD
kubectl port-forward svc/argocd-server -n argocd 8080:443
# https://localhost:8080 (admin/password)

# Prometheus
kubectl port-forward -n monitoring svc/prometheus-operated 9090:9090
# http://localhost:9090

# Grafana
kubectl port-forward -n monitoring svc/grafana 3000:80
# http://localhost:3000 (admin/admin)
```

### SSH Port Forwarding (for remote servers)

```bash
# From local machine (replace user@server with your details)
ssh -L 8080:localhost:8080 user@server kubectl port-forward svc/argocd-server -n argocd 8080:443
```

## Cost Optimization

### Monitor Costs

```bash
# Check current AWS costs
aws ce get-cost-and-usage \
  --time-period Start=2024-06-01,End=2024-06-30 \
  --granularity MONTHLY \
  --metrics "BlendedCost"
```

### Cost-Saving Tips

1. **Reduce Node Count**
   ```bash
   eksctl scale nodegroup --cluster=kronos --nodes=1 --name ng-xxxxx
   ```

2. **Use Spot Instances** (saves 70%)
   ```bash
   eksctl create nodegroup --cluster=kronos --spot
   ```

3. **Set Pod Limits**
   ```yaml
   resources:
     limits:
       memory: 256Mi
       cpu: 100m
   ```

4. **Delete Unused Resources**
   - Stop cluster when not in use
   - Delete S3 objects older than X days

## Troubleshooting

### Cluster Creation Fails

```bash
# Check AWS limits
aws ec2 describe-account-attributes --attribute-names max-instances

# Check region availability
aws ec2 describe-regions --all-regions

# Try with verbose output
eksctl create cluster --name kronos --region ap-south-1 --verbose 4
```

### Pods Not Starting

```bash
# Check pod events
kubectl describe pod <pod-name> -n <namespace>

# Check node resources
kubectl top nodes
kubectl top pods -A

# Check logs
kubectl logs <pod-name> -n <namespace>
```

### Cannot Connect to Services

```bash
# Verify service exists
kubectl get svc -n <namespace>

# Check if pods are running
kubectl get pods -n <namespace>

# Test connectivity from another pod
kubectl run -it --rm debug --image=busybox --restart=Never -- sh
# Inside the pod: curl http://service-name:port
```

### ArgoCD Password Issues

```bash
# Reset admin password
kubectl -n argocd patch secret argocd-secret \
  -p '{"data": {"admin.password": null}}'

# Restart ArgoCD server
kubectl rollout restart deployment/argocd-server -n argocd

# Get new initial password
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
```

## Performance Tuning

### Increase Node Count

```bash
aws eks update-nodegroup-config \
  --cluster-name kronos \
  --nodegroup-name ng-xxxxx \
  --scaling-config minSize=2,maxSize=5,desiredSize=3
```

### Increase Prometheus Retention

```bash
helm upgrade monitoring prometheus-community/kube-prometheus-stack \
  -n monitoring \
  --set prometheus.prometheusSpec.retention=60d
```

## Security Best Practices

1. ✅ Use IAM roles for service accounts (IRSA)
2. ✅ Enable VPC CNI security groups
3. ✅ Use network policies to restrict traffic
4. ✅ Encrypt data at rest and in transit
5. ✅ Regularly update cluster and nodes
6. ✅ Use private ECR repositories
7. ✅ Implement RBAC policies

## Next Steps

1. Deploy a sample application using ArgoCD
2. Create custom Grafana dashboards
3. Set up alerting rules
4. Integrate with CI/CD pipeline
5. Implement backup and disaster recovery

## Support & Documentation

- EKS Documentation: https://docs.aws.amazon.com/eks/
- Kubernetes Docs: https://kubernetes.io/docs/
- ArgoCD Guide: https://argo-cd.readthedocs.io/
- Prometheus Docs: https://prometheus.io/docs/

---

**Next**: Proceed to [Cleanup Guide](cleanup-guide.md) when you're ready to tear down resources.
