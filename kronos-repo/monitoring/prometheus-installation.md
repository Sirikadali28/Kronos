# Prometheus Installation Guide

## Overview

Prometheus is an open-source metrics collection and time-series database system. Combined with Grafana, it provides comprehensive observability for Kubernetes clusters.

## Prerequisites

- EKS cluster running with kubectl access
- Helm 3.12+ installed
- monitoring namespace created (`kubectl create namespace monitoring`)

## Installation Steps

### 1. Add Prometheus Helm Repository

First, add the Prometheus community Helm repository:

```bash
helm repo add prometheus-community \
  https://prometheus-community.github.io/helm-charts
```

### 2. Update Helm Repository

Fetch latest charts from the repository:

```bash
helm repo update
```

Expected output:
```
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "prometheus-community" chart repository
Update Complete. ⎉ Happy Helming!⎉
```

### 3. Install Prometheus Stack

Install the kube-prometheus-stack (includes Prometheus, Grafana, AlertManager, and more):

```bash
helm install monitoring \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set prometheus.prometheusSpec.retention=30d \
  --set grafana.adminPassword=admin
```

**What this installs:**
- Prometheus (metrics database)
- Grafana (visualization)
- Alertmanager (alerting)
- Node Exporter (node metrics)
- kube-state-metrics (Kubernetes metrics)

**Flags:**
- `retention=30d`: Keep metrics for 30 days
- `grafana.adminPassword`: Set Grafana admin password

### 4. Verify Installation

Check if all monitoring pods are running:

```bash
kubectl get pods -n monitoring
```

Expected output (wait 2-3 minutes):
```
NAME                                            READY   STATUS    RESTARTS   AGE
alertmanager-monitoring-xxxxx-0                 1/1     Running   0          2m
grafana-xxxxx                                   1/1     Running   0          2m
monitoring-kube-prometheus-operator-xxxxx       1/1     Running   0          2m
monitoring-prometheus-node-exporter-xxxxx       1/1     Running   0          2m
monitoring-prometheus-node-exporter-yyyyy       1/1     Running   0          2m
prometheus-monitoring-kube-prom-prometheus-0    1/1     Running   0          2m
```

All pods should show:
- READY = 1/1
- STATUS = Running

### 5. Check Services

View the created services:

```bash
kubectl get services -n monitoring
```

Expected services:
- alertmanager-operated
- grafana
- prometheus-operated
- kube-state-metrics
- node-exporter
- prometheus-operator

### 6. Access Prometheus

Port-forward to Prometheus:

```bash
kubectl port-forward -n monitoring \
  svc/prometheus-operated 9090:9090
```

Access: **http://localhost:9090**

You should see:
- Prometheus UI with alerts and targets
- "Targets" tab showing job status
- Query interface for PromQL

### 7. Access Grafana

Port-forward to Grafana:

```bash
kubectl port-forward -n monitoring \
  svc/grafana 3000:80
```

Access: **http://localhost:3000**

**Default login:**
- Username: `admin`
- Password: `admin` (or what you set during installation)

### 8. Verify Metrics Collection

#### Check if Prometheus is scraping targets:

Go to Prometheus UI (http://localhost:9090):
1. Click "Status" menu
2. Select "Targets"
3. Should see multiple jobs with "UP" status:
   - prometheus
   - kube-state-metrics
   - node-exporter
   - kubelet
   - kube-controller-manager
   - kube-scheduler

#### Run a test query in Prometheus:

Go to http://localhost:9090/graph and try:
```promql
# Check up/down status of targets
up

# CPU usage
rate(node_cpu_seconds_total[5m])

# Memory usage
node_memory_MemAvailable_bytes

# Pod count
count(kube_pod_info)
```

## Configuring Grafana Dashboards

### Add Prometheus Data Source

1. Go to Grafana (http://localhost:3000)
2. Click gear icon → Data Sources
3. Click "Add data source"
4. Select "Prometheus"
5. Set URL to: `http://prometheus-operated:9090`
6. Click "Save & Test"

### Import Pre-built Dashboards

1. Click "+" icon on left menu
2. Select "Import"
3. Dashboard ID examples:
   - `3662` - Prometheus stats
   - `3119` - Kubernetes cluster monitoring
   - `1860` - Node Exporter for Prometheus
4. Select data source (Prometheus)
5. Click "Import"

### Create Custom Dashboard

1. Click "+" → Dashboard
2. Click "Add new panel"
3. In query section, write PromQL:
   ```promql
   rate(container_cpu_usage_seconds_total[5m])
   ```
4. Configure visualization (graph, table, stat, etc.)
5. Click "Save dashboard"

## Monitoring Kubernetes Metrics

### Key Metrics to Monitor

**Node Metrics:**
```promql
# Node CPU usage
(1 - avg by (node) (irate(node_cpu_seconds_total{mode="idle"}[5m]))) * 100

# Node memory available
node_memory_MemAvailable_bytes / 1024 / 1024 / 1024

# Disk usage
node_filesystem_avail_bytes / node_filesystem_size_bytes * 100
```

**Pod Metrics:**
```promql
# Pod CPU usage
sum(rate(container_cpu_usage_seconds_total[5m])) by (pod_name)

# Pod memory usage
sum(container_memory_working_set_bytes) by (pod_name)

# Pod network traffic
sum(rate(container_network_transmit_bytes_total[5m])) by (pod_name)
```

**Cluster Metrics:**
```promql
# Number of nodes
count(node_info)

# Number of pods
count(kube_pod_info)

# Number of containers
count(container_last_seen)

# Cluster CPU allocation
sum(kube_pod_container_resource_requests_cpu_cores) / sum(kube_node_allocatable_cpu_cores)
```

## Alerting (AlertManager)

### Access AlertManager

```bash
kubectl port-forward -n monitoring \
  svc/alertmanager-operated 9093:9093
```

Access: **http://localhost:9093**

### Create Alert Rules

Alerts are configured in Prometheus. Default rules are included. Custom rules can be added via ConfigMaps.

View current rules:
```bash
kubectl get PrometheusRule -n monitoring
```

## Troubleshooting

### Prometheus Not Scraping Targets
```bash
# Check Prometheus logs
kubectl logs -n monitoring prometheus-monitoring-kube-prom-prometheus-0

# Verify configuration
kubectl get configmap -n monitoring prometheus-monitoring-kube-prom-prometheus

# Check if targets are reachable
kubectl exec -n monitoring prometheus-monitoring-kube-prom-prometheus-0 \
  -- curl -s localhost:9090/api/v1/targets | grep -i "error"
```

### Grafana Cannot Connect to Prometheus
```bash
# Test connectivity from Grafana pod
kubectl exec -n monitoring deployment/grafana -- \
  curl -v http://prometheus-operated:9090

# Check service DNS
kubectl exec -n monitoring deployment/grafana -- \
  nslookup prometheus-operated
```

### High Memory Usage
```bash
# Check Prometheus memory
kubectl top pod -n monitoring | grep prometheus

# Reduce retention or increase pod resources
helm upgrade monitoring \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set prometheus.prometheusSpec.retention=7d
```

### Storage Issues
```bash
# Check PVC status
kubectl get pvc -n monitoring

# Check disk space
kubectl exec -n monitoring prometheus-monitoring-kube-prom-prometheus-0 \
  -- df -h
```

## Updating Prometheus

### Check Current Version
```bash
kubectl get deployment -n monitoring
helm list -n monitoring
```

### Upgrade Stack
```bash
helm repo update
helm upgrade monitoring \
  prometheus-community/kube-prometheus-stack \
  -n monitoring
```

## Useful Commands

```bash
# View all Prometheus resources
kubectl get all -n monitoring

# Get Prometheus configuration
kubectl get secret -n monitoring prometheus-monitoring-kube-prom-prometheus -o json

# View Prometheus targets
kubectl port-forward -n monitoring svc/prometheus-operated 9090:9090
# Then visit http://localhost:9090/service-discovery

# Scale Prometheus replicas
kubectl scale statefulset prometheus-monitoring-kube-prom-prometheus \
  -n monitoring --replicas=2

# Check Prometheus disk usage
kubectl exec -n monitoring prometheus-monitoring-kube-prom-prometheus-0 \
  -- du -sh /prometheus
```

## Performance Tuning

### Increase Scrape Frequency
```bash
helm upgrade monitoring \
  prometheus-community/kube-prometheus-stack \
  -n monitoring \
  --set prometheus.prometheusSpec.scrapeInterval=15s
```

### Add Custom Scrape Configurations
```bash
kubectl edit ServiceMonitor -n monitoring
# Add new scrape targets
```

### Reduce Data Collection Size
```bash
helm upgrade monitoring \
  prometheus-community/kube-prometheus-stack \
  -n monitoring \
  --set prometheus.prometheusSpec.retention=7d \
  --set prometheus.prometheusSpec.walCompression=true
```

## Next Steps

1. [Create Custom Dashboards](../monitoring/grafana-installation.md)
2. [Set Up Alerting](../monitoring/monitoring-commands.md)
3. [Deploy Anomaly Detection Pipeline](../anomaly-detection/README.md)

## References

- Prometheus Documentation: https://prometheus.io/docs/
- Prometheus Community Helm Charts: https://github.com/prometheus-community/helm-charts
- PromQL Operators: https://prometheus.io/docs/prometheus/latest/querying/operators/
- Alerting Rules: https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
