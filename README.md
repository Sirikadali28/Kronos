
<p align="center">
  <img src="anomaly-detection/assets/branding/logo.png" width="120" alt="KRONOS Logo">
</p>

# KRONOS

<p align="center">
  <img src="anomaly-detection/assets/branding/banner.png" alt="KRONOS Banner">
</p>

<p align="center">
<strong>Production-Ready Cloud-Native Anomaly Detection Platform</strong>
</p>

<p align="center">
Building scalable, observable anomaly detection systems with modern DevOps practices.
</p>
------------------------------------------------------------------------
## 🏆 Status & Badges

<p align="center">

<img src="https://img.shields.io/github/license/Sirikadali28/Kronos?style=for-the-badge" alt="License">

<img src="https://img.shields.io/github/last-commit/Sirikadali28/Kronos?style=for-the-badge" alt="Last Commit">

<img src="https://img.shields.io/github/repo-size/Sirikadali28/Kronos?style=for-the-badge" alt="Repository Size">

<img src="https://img.shields.io/github/languages/top/Sirikadali28/Kronos?style=for-the-badge" alt="Top Language">

<img src="https://img.shields.io/github/v/release/Sirikadali28/Kronos?style=for-the-badge" alt="Latest Release">

<img src="https://img.shields.io/github/issues/Sirikadali28/Kronos?style=for-the-badge" alt="Open Issues">

<img src="https://github.com/Sirikadali28/Kronos/actions/workflows/ci.yml/badge.svg" alt="GitHub Actions">

</p>

```

------------------------------------------------------------------------

## 🗺️ Quick Navigation

```{=html}
<p align="center">
```
| [🎬 Demo](#demo) \| [🏗 Architecture](#system-architecture) \| [⚙️ Tech
  Stack](#technology-stack) \| [🚀 Quick Start](#quick-start) \| [📊
  Monitoring](#monitoring--observability) \| [🧪 Testing](#testing) \|

```{=html}
</p>
```

------------------------------------------------------------------------

## 📋 Table of Contents

-   [Overview](#overview)
-   [Project Highlights](#project-highlights)
-   [Project Metrics](#project-metrics)
-   [Key Features](#key-features)
-   [Technology Stack](#technology-stack)
-   [System Architecture](#system-architecture)
-   [Architecture Components](#architecture-components)
-   [Repository Structure](#repository-structure)
-   [Quick Start](#quick-start)
-   [Configuration](#configuration)
-   [Monitoring & Observability](#monitoring--observability)
-   [Testing](#testing)
-   [Deployment](#deployment)
-   [CI/CD Pipeline](#cicd-pipeline)
-   [Documentation](#documentation)
-   [Screenshots](#screenshots)
-   [Roadmap](#roadmap)
-   [Contributing](#contributing)
-   [License](#license)

------------------------------------------------------------------------

## Overview

**KRONOS** is a comprehensive cloud-native anomaly detection platform
that demonstrates production-grade engineering practices. It seamlessly
integrates Infrastructure as Code, GitOps, advanced observability, and
statistical anomaly detection algorithms into a robust, scalable system.

The platform is designed to detect statistical anomalies in real-time
data streams using multiple algorithms and ensemble voting, while
providing complete observability through Prometheus metrics and Grafana
dashboards.

------------------------------------------------------------------------
## Why KRONOS?

- Production-ready cloud-native architecture
- Infrastructure as Code using Terraform
- GitOps with ArgoCD
- Kubernetes-native deployment
- Enterprise monitoring with Prometheus & Grafana
- Statistical anomaly detection using ensemble algorithms
## 🚀 Project Highlights

This project showcases enterprise-level cloud-native development
practices with real-world implementations:

-   ✅ **Production-Ready FastAPI Backend** - Async, high-performance
    REST API with comprehensive error handling
-   ☸️ **Kubernetes Deployment on AWS EKS** - Auto-scaling,
    self-healing, fully managed Kubernetes
-   🏗️ **Infrastructure as Code with Terraform** - Reproducible,
    version-controlled infrastructure
-   🔄 **GitOps using ArgoCD** - Declarative deployments, automatic
    synchronization with Git
-   📊 **Statistical Anomaly Detection** - Z-Score, IQR, Moving Average,
    Ensemble Voting strategies
-   📈 **Prometheus Metrics & Grafana Dashboards** - Rich observability
    with pre-built dashboards
-   🐳 **Docker Containerization** - Multi-stage builds for optimized
    images
-   ⚡ **GitHub Actions CI/CD** - Automated testing, building, and
    deployment

------------------------------------------------------------------------

## 📈 Project Metrics

  Metric                       Value
  ---------------------------- ----------------------------------
  **Cloud Provider**           AWS EKS
  **Orchestration**            Kubernetes 1.27+
  **Programming Language**     Python 3.11+
  **Infrastructure as Code**   Terraform 1.5+
  **Backend Framework**        FastAPI 0.100+
  **Container Runtime**        Docker 20.10+
  **Monitoring & Metrics**     Prometheus 2.4x+ & Grafana 10.x+
  **GitOps Platform**          ArgoCD 2.x
  **CI/CD Pipeline**           GitHub Actions
  **Package Management**       Helm 3.x

------------------------------------------------------------------------

## ✨ Key Features

  -----------------------------------------------------------------------
  Feature                       Description
  ----------------------------- -----------------------------------------
  **FastAPI REST API**          Production-grade async Python API with
                                automatic OpenAPI documentation

  **Kubernetes Orchestration**  Cloud-native deployment with auto-scaling
                                and self-healing

  **AWS EKS**                   Managed Kubernetes on AWS with VPC
                                integration and security best practices

  **Infrastructure as Code**    Terraform modules for reproducible
                                infrastructure

  **ArgoCD GitOps**             Declarative deployments synced from Git
                                repositories

  **Multi-Algorithm Detection** Z-Score, IQR, Moving Average, and
                                Ensemble Voting strategies

  **Prometheus Metrics**        Rich metrics for all components with
                                custom anomaly detection metrics

  **Grafana Dashboards**        Pre-built dashboards for system health
                                and anomaly statistics

  **Docker Containerization**   Multi-stage builds for optimized
                                container images

  **CI/CD Pipeline**            GitHub Actions for automated testing and
                                deployment

  **Health Endpoints**          Liveness and readiness probes for
                                Kubernetes integration

  **Comprehensive Logging**     Structured JSON logging with ELK-stack
                                readiness
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## ⚙️ Technology Stack

```{=html}
<p align="center">
```
  -----------------------------------------------------------------------
  **Layer**            **Technology**                **Purpose**
  -------------------- ----------------------------- --------------------
  **Backend**          FastAPI                       High-performance
                                                     async REST API
                                                     framework

  **Language**         Python 3.11+                  Core application
                                                     development

  **Container**        Docker                        Containerization &
                                                     multi-stage builds

  **Orchestration**    Kubernetes                    Container
                                                     orchestration &
                                                     deployment

  **Cloud**            AWS EKS                       Managed Kubernetes
                                                     service

  **Infrastructure**   Terraform                     Infrastructure as
                                                     Code

  **Package Mgmt**     Helm                          Kubernetes package
                                                     management

  **GitOps**           ArgoCD                        Declarative
                                                     continuous
                                                     deployment

  **Monitoring**       Prometheus                    Metrics collection &
                                                     storage

  **Visualization**    Grafana                       Metrics dashboards &
                                                     alerting

  **Testing**          pytest                        Python testing
                                                     framework

  **CI/CD**            GitHub Actions                Automated pipelines
  -----------------------------------------------------------------------

```{=html}
</p>
```

------------------------------------------------------------------------

```
## 🏗️ System Architecture

<p align="center">
  <img src="assets/diagrams/architecture.png" width="100%" alt="KRONOS System Architecture">
</p>

KRONOS follows a cloud-native architecture where FastAPI processes incoming requests, statistical detection algorithms analyze time-series data, Kubernetes orchestrates workloads on Amazon EKS, and Prometheus with Grafana provide real-time observability.
## 🚀 Deployment Architecture

<p align="center">
  <img src="assets/diagrams/deployment.png" width="100%" alt="Deployment Architecture">
</p>
## 🔄 CI/CD Pipeline

<p align="center">
  <img src="assets/diagrams/cicd-pipeline.png" width="100%" alt="CI/CD Pipeline">
</p>
## 📊 Monitoring Architecture

<p align="center">
  <img src="assets/diagrams/monitoring.png" width="100%" alt="Monitoring Architecture">
</p>



------------------------------------------------------------------------

## 🏛️ Architecture Components

### **API Layer**

-   **FastAPI** - Async request handling, automatic OpenAPI docs
-   **Uvicorn** - ASGI server for high concurrency
-   **Pydantic** - Data validation and serialization

### **Detection Layer**

-   **Z-Score Detection** - Statistical method for outlier detection
-   **IQR (Interquartile Range)** - Robust outlier detection
-   **Moving Average** - Trend-based anomaly detection
-   **Ensemble Voting** - Multi-algorithm consensus voting

### **Infrastructure Layer**

-   **AWS EKS** - Managed Kubernetes cluster
-   **Terraform** - Infrastructure provisioning & management
-   **Helm** - Kubernetes package management
-   **ArgoCD** - GitOps deployment automation

### **Observability Layer**

-   **Prometheus** - Metrics collection and time-series database
-   **Grafana** - Data visualization and dashboards
-   **Custom Metrics** - Application-level anomaly metrics
-   **Structured Logging** - JSON-formatted log output

### **CI/CD & DevOps**

-   **GitHub Actions** - Automated testing and deployment
-   **Docker** - Container image building and optimization
-   **kubectl** - Kubernetes cluster management

------------------------------------------------------------------------

## 📂 Repository Structure

    KRONOS/
    ├── anomaly-detection/                # Core service
    │   ├── app/
    │   │   ├── main.py                  # FastAPI entry point
    │   │   ├── models.py                # Pydantic data models
    │   │   ├── detectors.py             # Detection algorithms
    │   │   ├── routes/
    │   │   │   ├── anomalies.py         # Detection endpoints
    │   │   │   ├── health.py            # Health check endpoints
    │   │   │   └── metrics.py           # Metrics endpoints
    │   │   └── utils/
    │   │       ├── logger.py            # Structured logging
    │   │       └── validators.py        # Input validation
    │   ├── tests/
    │   │   ├── unit/                    # Unit tests
    │   │   ├── integration/             # Integration tests
    │   │   └── load/                    # Performance tests
    │   ├── requirements.txt
    │   ├── Dockerfile
    │   └── .dockerignore
    │
    ├── terraform/                        # Infrastructure as Code
    │   ├── main.tf                      # EKS cluster config
    │   ├── variables.tf                 # Variable definitions
    │   ├── outputs.tf                   # Output values
    │   ├── vpc.tf                       # VPC & networking
    │   ├── security.tf                  # Security groups & IAM
    │   ├── backend.tf                   # Terraform state config
    │   ├── terraform.tfvars.example     # Example values
    │   └── modules/                     # Reusable modules
    │
    ├── kubernetes/                       # K8s manifests
    │   ├── namespace.yaml
    │   ├── deployments/
    │   │   ├── anomaly-detection.yaml
    │   │   ├── prometheus.yaml
    │   │   └── grafana.yaml
    │   ├── services/
    │   ├── ingress.yaml
    │   ├── configmaps/
    │   ├── secrets.example/
    │   └── persistent-volumes/
    │
    ├── argocd/                           # GitOps configuration
    │   ├── applications/
    │   │   ├── anomaly-detection-app.yaml
    │   │   ├── monitoring-app.yaml
    │   │   └── infrastructure-app.yaml
    │   └── argocd-config.yaml
    │
    ├── helm/                             # Helm charts (optional)
    │   └── kronos-chart/
    │       ├── Chart.yaml
    │       ├── values.yaml
    │       ├── values-prod.yaml
    │       └── templates/
    │
    ├── monitoring/                       # Observability configs
    │   ├── prometheus/
    │   │   ├── prometheus.yml           # Scrape configurations
    │   │   ├── alerts.yml               # Alert rules
    │   │   └── recording-rules.yml      # Recording rules
    │   ├── grafana/
    │   │   ├── dashboards/              # Pre-built dashboards
    │   │   ├── datasources/             # Prometheus datasource
    │   │   └── provisioning/
    │   └── loki/                        # Optional: Log aggregation
    │
    ├── .github/
    │   └── workflows/
    │       ├── test.yml                 # Automated testing
    │       ├── build.yml                # Docker image building
    │       └── deploy.yml               # Deployment pipeline
    │
    ├── docs/                             # Documentation
    │   ├── INSTALLATION.md              # Setup guide
    │   ├── DEPLOYMENT.md                # Deployment procedures
    │   ├── API.md                       # API documentation
    │   ├── ARCHITECTURE.md              # Architecture deep-dive
    │   ├── TROUBLESHOOTING.md           # Common issues
    │   └── CONTRIBUTING.md              # Dev guidelines
    │
    ├── assets/
    │   ├── branding/
    │   │   └── banner.png
    │   ├── diagrams/
    │   │   ├── architecture.png
    │   │   ├── deployment.png
    │   │   ├── cicd-pipeline.png
    │   │   └── monitoring.png
    │   └── screenshots/
    │
    ├── .gitignore
    ├── .dockerignore
    ├── .env.example
    ├── docker-compose.yml               # Local development
    ├── README.md
    ├── CHANGELOG.md
    ├── LICENSE
    └── Makefile                         # Helper commands

------------------------------------------------------------------------

## 🚀 Quick Start

### Prerequisites

-   Python 3.11+
-   Docker & Docker Compose
-   Kubernetes 1.27+ (for K8s deployment)
-   Terraform 1.5+ (for infrastructure)
-   kubectl configured
-   AWS account with EKS permissions (for cloud deployment)

### Local Development (5 minutes)

``` bash
# Clone repository
git clone https://github.com/Sirikadali28/Kronos.git
cd kronos

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
cd anomaly-detection
pip install -r requirements.txt

# Run application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Access the API:** - 🔗 Swagger UI: http://localhost:8000/docs - 📖
ReDoc: http://localhost:8000/redoc - ❤️ Health Check:
http://localhost:8000/health

### Docker Setup

``` bash
# Build image
docker build -t kronos:latest ./anomaly-detection

# Run with compose
docker-compose up -d

# Check logs
docker-compose logs -f anomaly-detection
```

### Kubernetes Deployment

``` bash
# Deploy all components
kubectl apply -f kubernetes/

# Verify deployment
kubectl get pods -n kronos
kubectl get svc -n kronos

# Access API locally
kubectl port-forward svc/anomaly-detection 8000:8000 -n kronos
```

### Infrastructure Deployment (AWS EKS)

``` bash
cd terraform

# Initialize
terraform init

# Review changes
terraform plan -out=tfplan

# Deploy infrastructure
terraform apply tfplan

# Get cluster credentials
aws eks update-kubeconfig --name kronos-cluster --region us-east-1

# Deploy applications
kubectl apply -f ../kubernetes/
```

------------------------------------------------------------------------

## 🔧 Configuration

### Environment Variables

Create `.env` from `.env.example`:

``` env
# API Configuration
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO
API_TITLE=KRONOS Anomaly Detection
API_VERSION=1.0.0

# Database (if applicable)
DATABASE_URL=postgresql://user:password@localhost/kronos

# AWS Configuration
AWS_REGION=us-east-1
AWS_EKS_CLUSTER_NAME=kronos-cluster

# Detection Settings
ANOMALY_THRESHOLD=2.5
DETECTION_WINDOW_SIZE=100
ENSEMBLE_VOTING_THRESHOLD=0.6

# Monitoring
PROMETHEUS_SCRAPE_INTERVAL=15s
GRAFANA_ADMIN_PASSWORD=your_secure_password
GRAFANA_ADMIN_USER=admin
```

### Terraform Variables

``` bash
cd terraform

# Create variables file
cp terraform.tfvars.example terraform.tfvars

# Edit with your values
nano terraform.tfvars
```

Key variables:

``` hcl
aws_region           = "us-east-1"
cluster_name         = "kronos-cluster"
cluster_version      = "1.27"
desired_capacity     = 2
max_capacity         = 5
min_capacity         = 1
```

------------------------------------------------------------------------

## 📊 Monitoring & Observability

### Prometheus

Access Prometheus metrics dashboard:

``` bash
kubectl port-forward svc/prometheus 9090:9090 -n monitoring
```

**URL**: http://localhost:9090

**Key Metrics**:

    anomaly_detection_total{algorithm="z_score"}
    anomaly_detection_latency_ms{percentile="p99"}
    algorithm_accuracy{detector="ensemble"}
    ensemble_voting_distribution
    detection_errors_total

### Grafana

Access Grafana dashboards:

``` bash
kubectl port-forward svc/grafana 3000:3000 -n monitoring
```

**URL**: http://localhost:3000 - **Username**: admin - **Password**:
(from environment config)

**Pre-built Dashboards**: - 📊 System Health - Pod resources, error
rates, uptime - 🚨 Anomaly Detection - Detection counts, confidence
scores - ⚡ Performance - Latency percentiles, throughput, response
times

### Health Checks

Kubernetes probes configured:

``` yaml
livenessProbe:
  httpGet:
    path: /health/live
    port: 8000
  initialDelaySeconds: 10
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health/ready
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 5
```

------------------------------------------------------------------------

## 🧪 Testing

Comprehensive test suite with multiple levels:

### Unit Tests

``` bash
pytest tests/unit/ -v
```

### Integration Tests

``` bash
pytest tests/integration/ -v
```

### Coverage Report

``` bash
pytest tests/ --cov=app --cov-report=html --cov-report=term
```

### Load Testing

``` bash
locust -f tests/load/load_test.py --host=http://localhost:8000
```

### All Tests

``` bash
pytest tests/ -v --cov=app --cov-report=html
```

**Coverage Target**: 85%+

------------------------------------------------------------------------

## 🚀 Deployment

### AWS EKS Deployment

``` bash
# Create EKS cluster
cd terraform
terraform apply

# Configure kubectl
aws eks update-kubeconfig --name kronos-cluster --region us-east-1

# Deploy with ArgoCD
kubectl apply -f ../argocd/

# Verify deployment
kubectl get all -n kronos
```

### Docker Image Building

``` bash
# Build
docker build -t kronos:latest ./anomaly-detection

# Push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URI
docker tag kronos:latest YOUR_ECR_URI/kronos:latest
docker push YOUR_ECR_URI/kronos:latest
```

### Rolling Update

``` bash
# Update image
kubectl set image deployment/anomaly-detection \
  anomaly-detection=YOUR_ECR_URI/kronos:v1.1.0 \
  -n kronos

# Monitor rollout
kubectl rollout status deployment/anomaly-detection -n kronos
```

### Rollback

``` bash
# View history
kubectl rollout history deployment/anomaly-detection -n kronos

# Rollback to previous version
kubectl rollout undo deployment/anomaly-detection -n kronos
```

------------------------------------------------------------------------

## 🔄 CI/CD Pipeline


### GitHub Actions Workflows

#### Test Pipeline (`.github/workflows/test.yml`)

Runs on every push: - Python linting (flake8) - Type checking (mypy) -
Unit tests (pytest) - Coverage report

#### Build Pipeline (`.github/workflows/build.yml`)

Triggered on tags: - Docker image build - Push to ECR - Create GitHub
release

#### Deploy Pipeline (`.github/workflows/deploy.yml`)

Manual or automatic: - Sync with ArgoCD - Update Kubernetes manifests -
Health checks - Rollback on failure

### Local Testing

``` bash
# Run all linting
black app/ && flake8 app/ && isort app/

# Type checking
mypy app/

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

------------------------------------------------------------------------

## 📚 Documentation

Comprehensive documentation available in `/docs`:

  -------------------------------------------------------------------------------------
  Document                                            Purpose
  --------------------------------------------------- ---------------------------------
  [**INSTALLATION.md**](docs/INSTALLATION.md)         Step-by-step setup guide

  [**DEPLOYMENT.md**](docs/DEPLOYMENT.md)             Production deployment procedures

  [**API.md**](docs/API.md)                           REST API reference documentation

  [**ARCHITECTURE.md**](docs/ARCHITECTURE.md)         System architecture deep-dive

  [**TROUBLESHOOTING.md**](docs/TROUBLESHOOTING.md)   Common issues and solutions

  [**CONTRIBUTING.md**](docs/CONTRIBUTING.md)         Development guidelines
  -------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 📸 Screenshots

> release.

Planned screenshots: - 🔗 **Swagger UI** - Interactive API
documentation - 📊 **Grafana Dashboard** - System health and anomaly
metrics - 🎯 **Prometheus Targets** - Scrape job status and metrics - 🔄
**ArgoCD Dashboard** - GitOps deployment status - ⚙️ **GitHub
Actions** - CI/CD pipeline execution - 📋 **Terraform Apply** -
Infrastructure deployment output

------------------------------------------------------------------------

## 🎬 Demo

Planned demo content: - Local deployment walkthrough - API usage
examples - Anomaly detection demonstration - Grafana dashboard tour -
Kubernetes deployment flow

------------------------------------------------------------------------

## 🗺️ Roadmap

### v1.0 - ✅ Released

-   [x] FastAPI backend with REST API
-   [x] Docker containerization
-   [x] Kubernetes deployment manifests
-   [x] Terraform infrastructure setup
-   [x] ArgoCD GitOps configuration
-   [x] Prometheus metrics integration
-   [x] Grafana dashboards
-   [x] GitHub Actions CI/CD pipelines
-   [x] Statistical anomaly detection algorithms
-   [x] Unit and integration tests
-   [x] Health check endpoints

### v1.1 - 🚀 In Progress

-   [ ] Extended test coverage (95%+ target)
-   [ ] Performance benchmarking suite
-   [ ] Demo video and screenshots
-   [ ] Helm chart optimization
-   [ ] Cost monitoring dashboard
-   [ ] Advanced alert rules
-   [ ] API documentation site

### v2.0 - 📋 Planned

-   [ ] Log aggregation (Loki/ELK)
-   [ ] Distributed tracing (Jaeger)
-   [ ] Machine learning model serving
-   [ ] Multi-region deployment
-   [ ] Advanced authentication (OAuth2)
-   [ ] Event streaming (Kafka)
-   [ ] Custom metrics exporters

### v2.1+ - 🔮 Future

-   [ ] Real-time data streaming pipelines
-   [ ] Advanced ML-based anomaly detection
-   [ ] Dashboard customization UI
-   [ ] Multi-tenant support
-   [ ] Cost optimization automations

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome! Follow these guidelines:

### Getting Started

1.  **Fork** the repository
2.  **Create** feature branch: `git checkout -b feature/amazing-feature`
3.  **Commit** changes: `git commit -m 'Add amazing feature'`
4.  **Push** branch: `git push origin feature/amazing-feature`
5.  **Open** Pull Request

### Development Setup

``` bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/ -v

# Format code
black app/ && isort app/

# Type checking
mypy app/
```

### Code Standards

-   **Style**: PEP 8 with Black formatter
-   **Types**: Type hints required for all functions
-   **Tests**: Minimum 80% coverage
-   **Docs**: Docstrings for all public APIs
-   **Commit**: Conventional commits (feat:, fix:, docs:, etc.)

### Pull Request Process

1.  Update documentation for any changes
2.  Add tests for new functionality
3.  Ensure all tests pass locally
4.  Update CHANGELOG.md
5.  Await code review

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **MIT License** - see
[LICENSE](LICENSE) file for details.

------------------------------------------------------------------------

## 🙋 Support

**Issues & Bugs**: [GitHub
Issues]https://github.com/Sirikadali28/Kronos/issues

**Feature Requests**: [GitHub
Discussionshttps://github.com/Sirikadali28/Kronos/issues

**Questions**: Open a discussion or check
[TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
---

Built with

Python • FastAPI • Docker • Kubernetes • AWS EKS • Terraform • Helm • ArgoCD • Prometheus • Grafana

⭐ If you found KRONOS useful, consider starring the repository.
------------------------------------------------------------------------

## 👨‍💻 Author

**Kadali Siri**

Cloud • DevOps • Backend Engineering

------------------------------------------------------------------------

```{=html}
<p align="center">
```
**[⬆ back to top](#kronos)**

```{=html}
</p>
```
