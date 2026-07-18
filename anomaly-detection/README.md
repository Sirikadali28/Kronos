# KRONOS: Cloud-Native Anomaly Detection Platform

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![AWS](https://img.shields.io/badge/AWS-EKS-FF9900.svg)
![Kubernetes](https://img.shields.io/badge/kubernetes-1.28+-326ce5.svg)

**A hands-on cloud-native implementation demonstrating anomaly detection workflows on Amazon EKS.**

KRONOS is a practical learning project that combines Kubernetes operations, GitOps practices, observability, and statistical anomaly detection to showcase modern cloud-native technologies. It demonstrates real-world deployment patterns, monitoring pipelines, and data-driven insights using production-grade tools.

---

## Project Overview

KRONOS demonstrates the implementation of:

* **Amazon EKS** for Kubernetes orchestration
* **Kubernetes** for workload management and validation
* **ArgoCD** for GitOps workflows
* **Prometheus and Grafana** for monitoring and observability
* **Python-based statistical anomaly detection**
* **Helm** for Kubernetes package management

The anomaly detection pipeline applies multiple statistical techniques to identify unusual patterns in time-series datasets and generates actionable reports.

---

## Implementation Evidence
EKS Cluster Provisioning

The following recording shows the successful creation of the EKS cluster using eksctl.

![EKS Provisioning](screenshots/eks-cluster-created.gif)

This provisioning process demonstrates:

- Successful EKS cluster creation
- Managed node group initialization
- Worker nodes reaching the Ready state
- Metrics Server addon installation
- kubeconfig setup for cluster access
### Amazon EKS

![EKS Cluster](screenshots/02-aws-eks-cluster-created.png)

### Worker Nodes

![EC2 Nodes](screenshots/06-ec2-instances-running-nodes.png)

### Grafana

![Grafana](screenshots/grafana-dashboard.png)

### ArgoCD

![ArgoCD](screenshots/argocd-dashboard.png)

### Anomaly Detection

![Output](screenshots/anomaly-output.png)

---

## Implementation Stages

### Stage 1: Amazon EKS Validation

Cluster connectivity and Kubernetes operations were validated using kubectl.

Validation commands:

```bash
kubectl get nodes
kubectl get pods -A
kubectl get namespaces
kubectl cluster-info
Evidence includes:
EKS Cluster Overview
Node Group Details
EC2 Worker Nodes
Cluster Health Validation
Stage 2: GitOps with ArgoCD
ArgoCD was deployed and validated to explore GitOps workflows.
Features explored:
Dashboard access
Application synchronization
Declarative deployment concepts
Application health monitoring
Stage 3: Observability Stack
Prometheus and Grafana were deployed using Helm.
Components:
Prometheus
Grafana
Helm
Capabilities validated:
Metrics collection
Dashboard visualization
Cluster observability
Monitoring workflow validation
Stage 4: Anomaly Detection Pipeline
The anomaly detection implementation uses multiple statistical techniques to identify abnormal behaviour in time-series data.
Implemented methods:
Z-Score Detection
Interquartile Range (IQR) Detection
Moving Average Analysis
Ensemble Voting
The pipeline generates anomaly reports and execution summaries.
Technologies Used
Table
Category	Technology
Cloud	Amazon EKS
Container Orchestration	Kubernetes
GitOps	ArgoCD
Monitoring	Prometheus
Visualization	Grafana
Package Management	Helm
CLI Tools	AWS CLI, kubectl
Analytics	Python
Libraries	Pandas, NumPy
Storage Validation	Amazon S3
Prerequisites
Install the following tools:
bash
aws --version
kubectl version --client
helm version
python --version
Configure AWS credentials before interacting with EKS.
Python Dependencies
Install required packages:
bash
pip install -r requirements.txt
requirements.txt includes: pandas, numpy, and other dependencies for the anomaly detection pipeline.
Deployment Scripts
The repository includes helper scripts for installing and validating selected components within an existing Kubernetes environment.
Install Prometheus and Grafana
bash
bash scripts/install-prometheus.sh
Install ArgoCD
bash
bash scripts/install-argocd.sh
Deploy the Anomaly Detection Pipeline
bash
bash scripts/deploy-anomaly.sh
Cleanup Resources
bash
bash scripts/uninstall.sh
Ensure AWS CLI, kubectl, and Helm are installed and configured before executing these scripts.
Repository Structure
Text
KRONOS/
├── README.md
├── LICENSE
├── requirements.txt
├── REPOSITORY_STRUCTURE.md
│
├── screenshots/
│   ├── eks-cluster-overview.png
│   ├── argocd-dashboard.png
│   ├── grafana-dashboard.png
│   └── anomaly-detection-output.png
│
├── kubernetes/
│   ├── cluster-commands.md
│   ├── deployment-notes.md
│   ├── namespaces.md
│   └── validation.md
│
├── monitoring/
│   ├── grafana-installation.md
│   └── monitoring-commands.md
│
├── argocd/
│   ├── login.md
│   └── commands.md
│
├── anomaly-detection/
│   ├── detect_anomalies.py
│   ├── sample_metrics.csv
│   ├── anomaly-output.txt
│   └── k8s/
│       └── job.yaml
│
├── scripts/
│   ├── install-prometheus.sh
│   ├── install-argocd.sh
│   ├── deploy-anomaly.sh
│   └── uninstall.sh
│
└── docs/
    ├── setup-guide.md
    ├── cleanup-guide.md
    └── lessons-learned.md
Anomaly Detection Pipeline
The anomaly detection pipeline combines multiple statistical techniques:
Z-Score Method
Identifies values significantly deviating from the mean.
Text
z = (x − μ) / σ
Anomaly if:
Text
|z| > 3
IQR Method
Robust outlier detection using quartiles.
Text
Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
Moving Average Method
Detects deviations from local trends.
Text
Deviation = |x − MA|
Ensemble Voting
Final anomalies are confirmed only when multiple methods agree.
This improves reliability and reduces false positives.
Kubernetes Job Execution
Unlike continuously running applications, the anomaly detector executes as a Kubernetes Job.
Workflow:
ConfigMap is generated from the anomaly detection script.
Kubernetes Job is created.
Statistical analysis is executed.
Reports are generated.
The Job terminates successfully.
Deploy:
bash
bash scripts/deploy-anomaly.sh
View logs:
bash
kubectl logs job/anomaly-detector
Monitoring Stack
The monitoring environment was deployed using Helm.
Components:
Prometheus
Grafana
Capabilities:
Cluster health monitoring
Metrics visualization
Operational validation
Dashboard exploration
GitOps with ArgoCD
ArgoCD was used to explore GitOps deployment workflows.
Activities included:
Dashboard access
Application synchronization
Health verification
Declarative deployment understanding
Additional Experiments
Additional cloud-native experiments included:
Amazon S3 validation
Istio exploration
Bookinfo sample application investigation
Service mesh observability concepts
Testing and Validation
The following activities were successfully validated:
EKS cluster accessibility
Worker node readiness
Kubernetes operations
ArgoCD deployment
Prometheus installation
Grafana dashboards
Statistical anomaly detection execution
S3 validation activities
Troubleshooting
Cluster Validation
bash
kubectl get nodes
kubectl get pods -A
kubectl get namespaces
kubectl cluster-info
ArgoCD
bash
kubectl get pods -n argocd
kubectl logs -n argocd deployment/argocd-server
Monitoring
bash
kubectl get pods -n monitoring
kubectl get svc -n monitoring
Anomaly Detection
bash
kubectl get jobs
kubectl logs job/anomaly-detector
Future Enhancements
Potential future improvements include:
Full GitOps auto-sync workflows
Service mesh implementation using Istio
Kiali integration
Real-time anomaly detection
CI/CD integration
Containerized anomaly detection images

## Challenges Faced

During the implementation of KRONOS, several practical challenges were encountered:

- Configuring Kubernetes access to the Amazon EKS cluster and validating the correct kubeconfig context.
- Troubleshooting Prometheus and Grafana deployments while understanding Helm chart configurations.
- Understanding ArgoCD concepts such as synchronization, application health, and declarative deployment workflows.
- Designing an anomaly detection approach that balanced accuracy and false positives using multiple statistical methods.
- Organizing the repository structure and documentation to accurately reflect the implementation process.
- Distinguishing between continuously running workloads and batch workloads, which led to using Kubernetes Jobs for anomaly detection execution.

These challenges provided valuable hands-on experience in debugging, problem-solving, and understanding cloud-native operational practices.
Author
Siri Kadali
B.Tech Student
Aditya College of Engineering and Technology
Focus Areas:
Cloud Computing
DevOps
Kubernetes
AWS
Observability
License
This project is licensed under the MIT License.
Status
Project Status: Completed as a hands-on cloud-native implementation and learning project.
Region: Asia Pacific (Mumbai)
This repository represents a practical cloud-native learning and implementation journey, demonstrating hands-on experience with Kubernetes operations, observability practices, GitOps workflows, and statistical anomaly detection.

