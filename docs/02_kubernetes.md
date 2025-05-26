# 🚢 Kubernetes Guide

## 🔧 What is Kubernetes?
Kubernetes (also known as K8s) is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.

- Developed by Google, now maintained by the Cloud Native Computing Foundation (CNCF)
- Works with Docker and other container runtimes
- Ensures high availability, scalability, and efficient resource usage

## 🧩 Core Concepts You’ll Use
- Pod: The smallest unit in Kubernetes. It runs one or more containers.
- Deployment: Makes sure your app is always running in the desired state (e.g., 2 pods running).
- Service: A stable network name (like a load balancer) to reach your pods.
- ConfigMap: Stores config files or environment variables (non-sensitive).
- Secret: Stores sensitive values like passwords or .env files.
- Namespace: A way to divide cluster resources for different projects or teams.


## 💡 Why Use Kubernetes?  
Automatically restarts crashed apps (self-healing)
Scales your app up/down based on traffic
Separates infrastructure logic from code using YAML files
Great for running microservices and using CI/CD
Cloud-agnostic: runs on your laptop, cloud, or hybrid

## 🧱 How We Use Kubernetes in This Project  
- **Microservices** (users, products) each run in their own Deployment
- Each has its own internal Service for communication
- An **Nginx Deployment + Service** handles external requests and routes traffic to services
- `.env` files are stored securely using **Secrets**
Will use **Helm** later to simplify managing these YAML files

## ⚙️ Common Kubernetes Components
1. Pod
    - Runs one or more containers together
    - Shares storage/network

2. Node
    - A machine (virtual or real) where containers run
    - Types:
        - Master Node: Controls everything
        - Worker Node: Runs your apps

3. Deployment
    - Keeps your app running as expected
    - Handles updates and scaling

4. Service
    - Lets other apps or users reach your Pods
    - Types:
        - ClusterIP: Default, for internal use
        - NodePort: Exposes app on a port on each node
        - LoadBalancer: External access (only on cloud)

5. ConfigMap
    - Keeps settings outside the app code
    - Example: Nginx config or API URLs

6. Secret
    - Keeps passwords, tokens, and env files secure

7. Namespace
    - Helps separate apps, like `dev/staging/prod` in the same cluster

## 🔁 How to Work with Kubernetes
1. Write a `Dockerfile` for each service
2. Build the image using Docker
3. Load the image into Minikube (or push to DockerHub)
4. Write Kubernetes YAML files
5. Apply them with `kubectl` apply
6. Monitor using `kubectl get pods`, etc.


## 🧪 Useful kubectl Commands  
```bash
# Check the cluster
kubectl get nodes

# See what’s running
kubectl get pods
kubectl get services
kubectl get deployments
kubectl get configmaps
kubectl get secrets

# Get more details or debug
kubectl describe pod <pod-name>
kubectl logs <pod-name>

# Apply or delete resources
kubectl apply -f <file-or-folder>
kubectl delete -f <file-or-folder>

# Access services locally
kubectl port-forward service/<service-name> <local-port>:<pod-port>

# Restart deployments
kubectl rollout restart deployment/<name>

# Create a secret from .env file
kubectl create secret generic <name> --from-file=./path/.env
```

## 📚 Learn More
* [Official Kubernetes Docs](https://kubernetes.io/docs/)
* [Kubernetes by Example](https://kubernetesbyexample.com/)
* CNCF Interactive Labs
