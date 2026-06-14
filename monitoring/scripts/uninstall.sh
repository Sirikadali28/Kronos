#!/bin/bash

helm uninstall prometheus -n monitoring

kubectl delete namespace monitoring --ignore-not-found
kubectl delete namespace argocd --ignore-not-found

kubectl delete -f anomaly-detection/k8s/deployment.yaml --ignore-not-found
kubectl delete -f anomaly-detection/k8s/configmap.yaml --ignore-not-found

echo "Cleanup completed."