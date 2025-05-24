# 🚀 Kubernetes Deployment for FastAPI E-commerce Microservices

This guide helps you deploy a microservices-based FastAPI project on **Kubernetes using Minikube** with locally built Docker images.


## 🛠️ Prerequisites

* Docker installed
* Minikube installed
* Kubernetes CLI (`kubectl`) installed
* Docker Compose installed (optional, if using compose to build images)

> **Note:** Ensure your `kubectl` and `minikube` versions are compatible for best results.


## ⚙️ Step-by-Step Deployment

### 📦 1. Build Docker Images Locally

Build your service images from their respective Dockerfiles:

```bash
docker build -t users-service:latest -f ./services/users/Dockerfile .
docker build -t products-service:latest -f ./services/products/Dockerfile .
```


### 🐳 2. Load Docker Images into Minikube

Since Minikube uses its own Docker daemon, you need to load these images into Minikube for Kubernetes to access them.

**Option 1 (Recommended):** Use Minikube’s image load command:

```bash
minikube image load users-service
minikube image load products-service
```

**Option 2:** Use Docker Compose inside Minikube’s Docker daemon:

```bash
# Switch Docker CLI context to Minikube's Docker daemon
eval $(minikube docker-env)

# Build images inside Minikube (using docker-compose.yml)
docker-compose build

# (Optional) Restore Docker CLI to your host
eval $(minikube docker-env -u)
```

> **Important:** When using local images in Kubernetes, set `imagePullPolicy: Never` or `IfNotPresent` in your deployment YAMLs to avoid Kubernetes trying to pull from a remote registry.


### 🔐 3. Create Kubernetes Secrets (if applicable)

If your services require environment variables or secrets, create them as Kubernetes secrets **before** applying your manifests:

```bash
kubectl create secret generic users-secret --from-file=./services/users/.env
kubectl create secret generic products-secret --from-file=./services/products/.env
```

Replace paths and secret names as per your setup.


### 🚀 4. Apply Kubernetes Manifests

Apply your deployment and service YAMLs:

```bash
kubectl apply -f k8s/base
```


### 🌐 5. Access the Application

To access your services, you have multiple options:

* **Expose nginx LoadBalancer service:**

  Minikube creates a tunnel for LoadBalancer services, which may show `<pending>` for EXTERNAL-IP.

  Use:

  ```bash
  minikube service nginx-service
  ```

  This command opens the nginx service URL in your default browser.

* **Port-forward individual services (ClusterIP):**

  If your users-service and products-service are `ClusterIP`, forward their ports locally:

  ```bash
  kubectl port-forward service/users-service 8000:80
  kubectl port-forward service/products-service 8001:80
  ```

  Then access these URLs in your browser:

  * [http://localhost:8000/docs](http://localhost:8000/docs) → Users service Swagger UI
  * [http://localhost:8001/docs](http://localhost:8001/docs) → Products service Swagger UI


### 🔍 6. Useful Commands and Troubleshooting

* Check pods status:

  ```bash
  kubectl get pods
  ```

* Describe a pod for detailed info:

  ```bash
  kubectl describe pod <pod-name>
  ```

* View logs of a pod:

  ```bash
  kubectl logs <pod-name>
  ```

* Restart a deployment after rebuilding images:

  ```bash
  kubectl rollout restart deployment/products-deployment
  ```

* Delete all applied Kubernetes resources:

  ```bash
  kubectl delete -f k8s/base
  ```

* Check Minikube status and logs:

  ```bash
  minikube status
  minikube logs
  ```

* Troubleshoot common pod issues:

  * `ImagePullBackOff` or `ErrImagePull`: Check `imagePullPolicy`, ensure image is loaded into Minikube.
  * `CrashLoopBackOff`: Check pod logs for runtime errors.
  * Secret not found: Verify secrets are created before pods start.


## 📌 Notes

* Kubernetes defaults to the `default` namespace; if you use a custom namespace, add `-n <namespace>` to your `kubectl` commands.
* Your Dockerfiles don’t need to set environment variables if you use Kubernetes secrets or ConfigMaps to inject them.
* When mounting ConfigMaps (e.g., for nginx config), remember to restart pods if you update ConfigMaps to apply changes.
* Minikube’s LoadBalancer is different from cloud providers: it uses a tunnel, so EXTERNAL-IP will be `<pending>`. Use `minikube service` to access the service.

