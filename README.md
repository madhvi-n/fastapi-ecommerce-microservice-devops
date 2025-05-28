# FastAPI Ecommerce Microservice DevOps Project
[![Docker Image CI](https://github.com/madhvi-n/fastapi-ecommerce-microservice-devops/actions/workflows/docker-image.yml/badge.svg)](https://github.com/madhvi-n/fastapi-ecommerce-microservice-devops/actions/workflows/docker-image.yml)
[![CodeQL Advanced](https://github.com/madhvi-n/fastapi-ecommerce-microservice-devops/actions/workflows/codeql.yml/badge.svg)](https://github.com/madhvi-n/fastapi-ecommerce-microservice-devops/actions/workflows/codeql.yml)
[![FastAPI CI](https://github.com/madhvi-n/fastapi-ecommerce-microservice-devops/actions/workflows/python-app.yml/badge.svg)](https://github.com/madhvi-n/fastapi-ecommerce-microservice-devops/actions/workflows/python-app.yml)
![Kubernetes](https://img.shields.io/badge/k8s-ready-blueviolet)


## 🚀 Project Overview
This project demonstrates deploying a microservices-based FastAPI e-commerce application using modern DevOps tooling and best practices:

* **Microservices**: users and products services built with FastAPI.
* **Containerization**: Docker for packaging apps.
* **Orchestration**: Kubernetes (Minikube) for deployment and scaling.
* **Configuration Management**: Helm charts for templating Kubernetes manifests.
* **Infrastructure as Code**: Terraform for provisioning cloud resources.
* **Monitoring & Observability**: Prometheus + Grafana for metrics; ELK Stack for logging.
* **CI/CD**: Automated pipelines for build, test, and deployment.


## Features
- Microservices architecture with independent services for users, products, and more
- Authentication with OAuth (Google, GitHub)
- Role-based access control (Admin, Staff, Customer roles)
- PostgreSQL or SQLite database support via SQLAlchemy ORM
- JWT token authentication
- Dockerized services for consistent environments
- Kubernetes manifests for container orchestration
- Terraform integration for cloud infrastructure (planned)

## 📦 Prerequisites
- [x] Docker
- [x] Minikube & kubectl
- [x] Helm
- [ ] Terraform
- [ ] Prometheus + Grafana (Optional)
- [ ] ELK Stack (Optional)


### 🛠 Setup & Deployment

### Initial SetUp
1. Clone the repo:

   ```bash
   git clone https://github.com/madhvi-n/fastapi-ecommerce-microservice-devops.git
   cd fastapi-ecommerce-microservice-devops
   ```

2. Environment variables
Refer to `services/users/.env.example` for required variables like:
- `DATABASE_URL`
- `JWT_SECRET_KEY`
- `GOOGLE_CLIENT_ID`


### 1. Build and load Docker images
Build service images locally:
```bash
docker build -t users-service:latest -f ./services/users/Dockerfile .
docker build -t products-service:latest -f ./services/products/Dockerfile .
```

Load images into Minikube’s Docker daemon:
```bash
minikube image load users-service
minikube image load products-service
```

### 2. Deploy with Kubernetes [K8 deployment guide](./deployment-guides/k8-deployment-guide.md)
Apply base Kubernetes manifests (deployments, services, configmaps, secrets):

```bash
kubectl apply -f k8s/base
```
Use Helm charts for easier management [Helm deployment guide](./deployment-guides/helm-deployment-guide.md)

```bash
helm install users ./helm-chart/users
helm install products ./helm-chart/products
```

Use ingress [Ingress deployment guide](./deployment-guides/ingress-deployment-guide.md)
```bash
kubectl apply -f ingress.yaml

# Check if ingress is created
kubectl get ingress

# Check if ingress is running
kubectl get pods -n ingress-nginx
```

Now you can access your services from your browser:

```bash
http://app.local/users
http://app.local/products
```


### 3. Infrastructure Provisioning with Terraform (Locally)
Use Terraform to provision cloud infrastructure resources (e.g., AWS S3 buckets, databases, etc.):
```bash
terraform init
terraform apply

```

### 4. Monitoring & Logging
- **Prometheus + Grafana:** Monitor app and cluster metrics with real-time dashboards.
- **ELK Stack:** Centralized log collection and analysis across services.


### 🔧 Useful Commands
```bash
# Kubernetes commands
kubectl get pods
kubectl get svc
kubectl logs <pod-name>
kubectl port-forward service/nginx-service 8080:80

# Helm commands
helm install ecommerce ./helm-chart
helm upgrade ecommerce ./helm-chart
helm uninstall ecommerce

# Terraform commands
terraform init
terraform plan
terraform apply
terraform destroy

# Docker commands
docker build -t users-service:latest ./services/users
docker push <registry>/users-service:latest
docker-compose up
docker-compose build
docker-compose down
```

## 🧰 DevOps Toolkit Overview
### Docker
* Containerize microservices for consistent environments.

### Kubernetes (Minikube + kubectl)
* Orchestrate deployment, scaling, and management of containers.

### Helm
* Package and manage Kubernetes manifests as charts for templating and reusability.

### Terraform
* Infrastructure as code to provision and manage cloud resources.

### Prometheus & Grafana
* Monitor system and application metrics with dashboards and alerts.

### ELK Stack (Elasticsearch, Logstash, Kibana)
* Centralized logging and visualization for troubleshooting and auditing.

### CI/CD
* Automate build, test, and deployment for rapid and reliable delivery.


## 💡 Future Enhancements:
- [ ] GitHub Actions or Jenkins for CI/CD
- [ ] Docker Hub or GitHub Container Registry
- [ ] Istio or Linkerd for service mesh
- [ ] ELK stack (Elasticsearch, Logstash, Kibana) or Loki or Jaeger for logging/tracing
- [ ] Vault or Sealed Secrets for secret management
- [ ] Ansible, Chef, Puppet for Configuration management
<!-- - [ ] AWS CLI, Azure CLI, Google Cloud SDK for Cloud APIs -->
<!-- - [ ] MetalLB (for bare metal K8s) or NGINX Ingress Controller or Traefik — ingress management for Networking / Load Balancers -->


## 📚 References
- [Docker Docs](https://docs.docker.com/)
- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Helm Docs](https://helm.sh/docs/)
- [Terraform Docs](https://developer.hashicorp.com/terraform/docs)
- [Prometheus Docs](https://prometheus.io/docs/)
- [Grafana Docs](https://grafana.com/docs/)
- [Elastic Stack Docs](https://www.elastic.co/guide/index.html)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
