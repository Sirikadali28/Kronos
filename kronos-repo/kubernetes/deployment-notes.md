**# Deployment Notes**



**## Cluster Details**



**- Cluster Name: kronos**

**- Region: ap-south-1**

**- Kubernetes Version: 1.34**



**## Worker Nodes**



**- Instance Type: t3.small**

**- Desired Nodes: 2**

**- Minimum Nodes: 1**

**- Maximum Nodes: 2**



**## Monitoring Stack**



**The monitoring stack was deployed using Helm charts and validated using Kubernetes commands.**



**Components included:**



**- Prometheus**

**- Grafana**



**## GitOps**



**ArgoCD was configured and accessed successfully for deployment management.**



**## Validation**



**The environment was validated using:**



**```bash**

**kubectl get nodes**

**kubectl get pods -A**

**kubectl get namespaces**

**```**

