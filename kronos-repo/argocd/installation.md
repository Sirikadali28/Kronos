# ArgoCD Installation Guide

## Overview

ArgoCD is a declarative, GitOps continuous delivery tool for Kubernetes. It enables automated deployment of applications stored in Git repositories.

## Prerequisites

- EKS cluster running (verified with `kubectl cluster-info`)
- kubectl configured to access the cluster
- Access to argocd namespace (will be created)

## Installation Steps

### 1. Create argocd Namespace
```bash
kubectl create namespace argocd
```

Verify:
```bash
kubectl get namespace argocd
```

Expected output:
```
NAME     STATUS   AGE
argocd   Active   10s
```

### 2. Install ArgoCD

Download and apply the official ArgoCD manifest:

```bash
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

This installs:
- ArgoCD API server
- ArgoCD repository server
- ArgoCD controller manager
- ArgoCD application controller
- ArgoCD dex (authentication)

### 3. Verify Installation

Check if all ArgoCD pods are running:

```bash
kubectl get pods -n argocd
```

Expected output (wait 2-3 minutes for all pods to be Ready):
```
NAME                                            READY   STATUS    RESTARTS   AGE
argocd-application-controller-0                 1/1     Running   0          2m
argocd-applicationset-controller-0              1/1     Running   0          2m
argocd-dex-server-xxx                           1/1     Running   0          2m
argocd-metrics-server-xxx                       1/1     Running   0          2m
argocd-notifications-controller-xxx             1/1     Running   0          2m
argocd-redis-xxx                                1/1     Running   0          2m
argocd-repo-server-xxx                          1/1     Running   0          2m
argocd-server-xxx                               1/1     Running   0          2m
```

All pods should have:
- READY = 1/1
- STATUS = Running

### 4. Port Forward to Access Web UI

ArgoCD server isn't exposed externally by default. Use port-forward:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Then access: **https://localhost:8080**

(Note: You'll get a self-signed certificate warning - this is expected)

### 5. Retrieve Initial Admin Password

The admin password is stored in a Kubernetes secret:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
```

Example output:
```
ABC123xyz-RandomPassword-xyz789
```

**Save this password** - you'll need it to login initially.

### 6. First Login

1. Go to **https://localhost:8080**
2. Username: `admin`
3. Password: (from above command)
4. Click "Login"

You should see the ArgoCD dashboard showing:
- No applications (empty state)
- Navigation menu on left
- Settings and user options

### 7. Change Admin Password

For security, change the initial admin password:

#### Option A: Using Web UI
1. Click user icon (top right)
2. Select "User Info"
3. Click "Update Password"
4. Enter current and new password

#### Option B: Using ArgoCD CLI
```bash
# Install ArgoCD CLI (if not already installed)
curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
chmod +x ./argocd

# Login with CLI
./argocd login localhost:8080 \
  --username admin \
  --password <initial-password> \
  --insecure

# Change password
./argocd account update-password \
  --account admin \
  --current-password <initial-password> \
  --new-password <new-password>
```

## Adding a Git Repository (Optional)

To enable GitOps deployments, connect a Git repository:

### Via Web UI
1. Settings (left menu) → Repositories
2. "Connect Repo Using HTTPS" or SSH
3. Enter repository URL
4. Provide credentials if private repo

### Via CLI
```bash
argocd repo add https://github.com/your-username/your-repo.git \
  --username <git-username> \
  --password <git-token>
```

## Creating an Application (Optional)

Deploy an application using ArgoCD:

### Via Web UI
1. Click "Create Application"
2. Fill in:
   - Application Name
   - Project: default
   - Repository URL
   - Path: (path to manifests in repo)
   - Cluster: https://kubernetes.default.svc
   - Namespace: default (or your namespace)
3. Click "Create"

### Via CLI
```bash
argocd app create my-app \
  --repo https://github.com/your-username/your-repo.git \
  --path ./ \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default
```

## Monitoring Application Health

### Check Application Status
```bash
# List all applications
kubectl get applications -n argocd

# Detailed application status
kubectl describe application <app-name> -n argocd

# Sync status
argocd app list
```

### View Application Details
```bash
# Get all resources managed by app
argocd app resources <app-name>

# Check sync status
argocd app get <app-name>
```

## GitOps Workflow

Once configured, the workflow is:

1. **Commit changes to Git**: Push manifests to repository
2. **ArgoCD monitors Git**: Continuously watches for changes
3. **Detect differences**: Compares desired (Git) vs actual (cluster)
4. **Sync**: Automatically applies changes (if auto-sync enabled)

### Enable Auto-Sync
```bash
argocd app set <app-name> --sync-policy automated
```

### Manual Sync
```bash
# Sync application with Git
argocd app sync <app-name>

# Sync and wait for completion
argocd app sync <app-name> --wait
```

## Troubleshooting

### ArgoCD Server Not Accessible
```bash
# Check if service exists
kubectl get svc -n argocd

# Check pod logs
kubectl logs -n argocd deployment/argocd-server

# Verify namespace
kubectl get pods -n argocd
```

### Cannot Retrieve Admin Password
```bash
# Check if secret exists
kubectl get secret -n argocd argocd-initial-admin-secret

# If missing, get any existing secret
kubectl get secrets -n argocd
```

### Application Not Syncing
```bash
# Check application status
kubectl describe application <app-name> -n argocd

# Check repository connection
argocd repo list

# View application events
kubectl get events -n argocd | grep <app-name>
```

### Port Forward Issues
```bash
# Kill existing port-forward
pkill -f "port-forward"

# Try again with verbose output
kubectl port-forward svc/argocd-server -n argocd 8080:443 -v 4
```

## Useful ArgoCD Commands

```bash
# List all applications
argocd app list

# Get application details
argocd app get <app-name>

# View application logs
argocd app logs <app-name>

# Sync application
argocd app sync <app-name>

# Delete application
argocd app delete <app-name>

# Check ArgoCD version
argocd version

# List connected repositories
argocd repo list

# Delete a repository
argocd repo rm <repo-url>
```

## Security Best Practices

1. ✅ Changed initial admin password
2. ✅ Restricted argocd namespace access
3. ✅ Used RBAC for ArgoCD access
4. ✅ Stored Git credentials securely in Kubernetes secrets
5. ✅ Used HTTPS for repository connections (when possible)

## Next Steps

1. [Prometheus Monitoring Setup](../monitoring/prometheus-installation.md)
2. [Anomaly Detection Pipeline](../anomaly-detection/README.md)
3. Deploy sample application using GitOps

## References

- ArgoCD Documentation: https://argo-cd.readthedocs.io/
- ArgoCD GitHub: https://github.com/argoproj/argo-cd
- Kubernetes Secrets: https://kubernetes.io/docs/concepts/configuration/secret/
