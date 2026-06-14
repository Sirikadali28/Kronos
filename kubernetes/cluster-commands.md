**# Kubernetes Cluster Commands**



**These commands were used to validate and interact with the EKS cluster during implementation.**



**## Verify Current Context**



**```bash**

**kubectl config current-context**

**```**



**## Check Cluster Information**



**```bash**

**kubectl cluster-info**

**```**



**## View Nodes**



**```bash**

**kubectl get nodes -o wide**

**```**



**## View All Namespaces**



**```bash**

**kubectl get namespaces**

**```**



**## View Pods Across All Namespaces**



**```bash**

**kubectl get pods -A**

**```**



**## View Services**



**```bash**

**kubectl get svc -A**

**```**



**## Describe a Node**



**```bash**

**kubectl describe node <node-name>**

**```**

