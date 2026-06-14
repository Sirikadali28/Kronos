**# Kubernetes Namespaces**



**The following namespaces were observed and validated during the KRONOS implementation.**



**## Default Namespaces**



**```bash**

**kubectl get namespaces**

**```**



**Example output:**



**```**

**default**

**kube-node-lease**

**kube-public**

**kube-system**

**```**



**## Additional Namespaces**



**Namespaces created during the project included monitoring and GitOps components.**



**Examples:**



**- argocd**

**- monitoring**



**Verify:**



**```bash**

**kubectl get namespaces**

**```**

