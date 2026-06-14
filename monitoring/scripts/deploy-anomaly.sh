#!/bin/bash

kubectl apply -f anomaly-detection/k8s/configmap.yaml
kubectl apply -f anomaly-detection/k8s/deployment.yaml

kubectl get pods

echo "Anomaly detector deployed."