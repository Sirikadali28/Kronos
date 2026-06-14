**# Environment Validation**



**The following checks were performed to confirm successful deployment.**



**## Node Validation**



**```bash**

**kubectl get nodes**

**```**



**Expected outcome:**



**- All worker nodes are in Ready state.**



**---**



**## Pod Validation**



**```bash**

**kubectl get pods -A**

**```**



**Expected outcome:**



**- System pods are running.**

**- Monitoring components are healthy.**

**- ArgoCD components are operational.**



**---**



**## Namespace Validation**



**```bash**

**kubectl get namespaces**

**```**



**Expected outcome:**



**- Required namespaces are present.**



**---**



**## Cluster Health**



**```bash**

**kubectl cluster-info**

**```**



**Expected outcome:**



**- Kubernetes control plane endpoints are accessible.**

