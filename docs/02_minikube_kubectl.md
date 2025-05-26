# Minikube + kubectl Guide

## 🔧 What is Minikube?

Minikube is a tool that lets you run a single-node Kubernetes cluster locally for development and testing.

* Ideal for learning and prototyping Kubernetes locally
* Spins up a lightweight virtual machine or container with Kubernetes
* Comes with built-in Kubernetes tools and dashboard

## 🔧 What is kubectl?

kubectl is the command-line interface for interacting with Kubernetes clusters. It allows you to deploy applications, inspect and manage cluster resources, and view logs.

## Key Concepts Used in This Project

* **Minikube Cluster**: A local Kubernetes cluster created and managed by Minikube.
* **kubectl Context**: Minikube sets the current kubectl context to its local cluster.
* **Image Loading**: Locally built Docker images can be loaded into Minikube.

## Why Use Minikube?

* Easy to set up and run Kubernetes locally
* Great for development and testing
* Supports volume mounts, load balancer simulation, and ingress controllers
* No need for cloud provider to experiment with Kubernetes

## How We Use Minikube + kubectl in This Project

* Minikube runs the local Kubernetes cluster.
* kubectl is used to deploy microservices and manage pods/services.
* We use `minikube image load` to load local Docker images into the Minikube VM.
* We expose services with `minikube service` or `kubectl port-forward`.

## Basic Minikube Commands

* `minikube start` — start the local cluster
* `minikube stop` — stop the cluster
* `minikube status` — show cluster status
* `minikube dashboard` — launch the GUI dashboard
* `minikube delete` — delete the cluster
* `minikube image load <image-name>` — load Docker image into Minikube
* `minikube service <service-name>` — open a service in your browser

## Basic kubectl Commands

* `kubectl get pods` — list running pods
* `kubectl get svc` — list services
* `kubectl logs <pod>` — see pod logs
* `kubectl apply -f <file>` — apply manifest file
* `kubectl delete -f <file>` — delete resources
* `kubectl port-forward service/<service-name> <local-port>:<container-port>` — access ClusterIP services locally

## 🧱 Key Minikube & kubectl Components

### 1. **Minikube VM**

* Runs a lightweight Kubernetes cluster
* Uses Docker, Podman, or VirtualBox depending on configuration

### 2. **kubectl Context**

* kubectl switches to use Minikube context after `minikube start`
* You can check current context with `kubectl config current-context`

### 3. **Image Management**

* Load local images using `minikube image load` (without needing a registry)
* Or use `eval $(minikube docker-env)` to build inside Minikube's Docker daemon

### 4. **Service Exposure**

* Use `minikube service` to expose a LoadBalancer-type service on localhost
* Use `kubectl port-forward` for ClusterIP services

## 🔁 Minikube + kubectl Workflow

1. Start Minikube cluster
2. Build Docker image for each service
3. Load image into Minikube using `minikube image load`
4. Apply Kubernetes manifests using `kubectl apply`
5. Monitor pods/services using `kubectl get pods` / `kubectl get svc`
6. Access services via `minikube service` or port forwarding

## 📦 Common Commands Summary

```bash
# Start/Stop cluster
minikube start
minikube stop

# Load Docker images
minikube image load <image-name>

# View status
minikube status
minikube dashboard

# Interact with services
minikube service <service-name>
kubectl port-forward service/<service-name> <local-port>:<container-port>

# Work with Kubernetes manifests
kubectl apply -f <file.yaml>
kubectl delete -f <file.yaml>
kubectl get pods
kubectl logs <pod-name>
```

## 📚 Further Reading

* [Minikube Docs](https://minikube.sigs.k8s.io/docs/)
* [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
* [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
