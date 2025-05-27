# 🚀 Helm Deployment Guide for FastAPI Microservices on Minikube
This guide helps you deploy your microservices (e.g., users, products) to a local Kubernetes cluster using Minikube and Helm.

## 🧰 Prerequisites
Make sure the following tools are installed:
* Docker
* Minikube
* Kubectl
* Helm

## 🟢 Step 1: Start Minikube
```bash
minikube start
```
Enable Docker environment in Minikube:

```bash
eval $(minikube docker-env)
```
This ensures Docker images are built inside Minikube's Docker daemon.

## 🐳 Step 2: Build Docker Images
Navigate to your project root and build images for your services:

```bash
docker build -t users-service:latest ./services/users/Dockerfile .
docker build -t products-service:latest ./services/products/Dockerfile .
```

## 📦 Step 3: Create Helm Charts
You should already have charts like this:

```bash
helm-charts/
  ├── users/
  │   ├── Chart.yaml
  │   ├── values.yaml
  │   ├── templates/
  │   │   ├── deployment.yaml
  │   │   ├── service.yaml
  │   │   ├── secret.yaml
```
Make sure each `values.yaml` contains the correct config and `env:` block.


## 📤 Step 4: Deploy Microservices via Helm
From the root of your project:

```bash
helm install users ./helm-charts/users
helm install products ./helm-charts/products
```
To upgrade later:

```bash
help upgrade --install users ./helm-charts/users
```

## 🔍 Step 5: Verify Deployments
```bash
kubectl get pods
kubectl get svc
```

## 🌐 Step 6: Access the App Locally
```bash
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=users-service-charts,app.kubernetes.io/instance=users" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
kubectl --namespace default port-forward $POD_NAME 8081:$CONTAINER_PORT

export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=products-service-charts,app.kubernetes.io/instance=products" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
kubectl --namespace default port-forward $POD_NAME 8082:$CONTAINER_PORT
```
Then open: `http://localhost:8081/docs`

OR

```bash
kubectl port-forward svc/users-users-service-charts 8000:8000
kubectl port-forward svc/users-users-service-charts 8001:8000
```
Then open: `http://localhost:8000/health` or `http://localhost:8081/docs`

## 🛑 Step 7: Cleanup
```bash
helm uninstall users
helm uninstall products
minikube delete
```

✅ Next Steps
* Add Ingress for easier routing
* Set up CI/CD with Jenkins
* Add ELK stack for logs
* Use Ansible for provisioning

