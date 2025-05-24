# Project Design Overview: E-Commerce with FastAPI, NGINX, and Docker

## 🔧 Tech Stack

* **Backend Framework**: FastAPI (Python)
* **API Gateway**: NGINX
* **Containerization**: Docker
* **Orchestration**: Docker Compose
* **Architecture**: Microservices (users, products, etc.)


## 📦 Folder Structure

```
ecommerce-fastapi/
├── services/
│   ├── users/
│   └── products/
├── nginx.conf
├── docker-compose.yml
├── README.md
└── DESIGN.md
```


## 🧹 Microservice Architecture

Each domain (users, products) is built as an **independent FastAPI app** with its own:

* Codebase
* `.env` file
* Dockerfile

This allows:

* Independent development and deployment
* Easier scaling per service
* Better separation of concerns


## 🌐 API Gateway (NGINX)

We placed **NGINX** at the root level to avoid unnecessary directories like `api-gateway/`.

NGINX is used for:

* **Reverse proxy**: Routes requests from `/users/*`, `/products/*` to the corresponding backend container
* **Single entry point**: Clients only interact with `http://localhost`

### Example Routing:

```nginx
location /users/ {
    proxy_pass http://users:8000/;
}
location /products/ {
    proxy_pass http://products:8000/;
}
```


## 🐳 Docker Compose

All services are defined in `docker-compose.yml`.

### Key Decisions:

* **Expose only NGINX on host (port 80)**: Microservices use `expose` so they're accessible only within the Docker network.
* **No port conflicts**: Each service runs on `8000` **inside** its own container, and NGINX handles path-based routing.
* **Shared `.env` isolation**: Each service loads its own `.env` without leaking secrets to GitHub.


## 🛡️ Security

* `.env` files are **git-ignored** to prevent secret leakage
* Use `expose` (not `ports`) for internal services
* Plan to integrate HTTPS in production


## 🚀 Deployment Flow

```bash
# Start everything
sudo docker-compose up --build

# Remove containers
sudo docker-compose down --rmi all --volumes --remove-orphans
```

Access the app:

* `http://localhost/users/`
* `http://localhost/products/`


## 🥪 Future Improvements

* CI/CD integration via GitHub Actions
* Add Let's Encrypt + HTTPS to NGINX
* Add logging/monitoring (e.g., Prometheus, Grafana)
* Introduce service discovery (if scaling beyond Docker Compose)


## 🤝 Summary of Decisions

| Decision                        | Reason                                             |
| ------------------------------- | -------------------------------------------------- |
| Microservices (not monolith)    | Modular, scalable, maintainable                    |
| NGINX as API Gateway            | Centralized routing, cleaner port management       |
| Single exposed port (80)        | Simplicity and security                            |
| Isolated `.env` per service     | Environment safety and CI compatibility            |
| Docker Compose + internal ports | Avoids port conflicts; enables container isolation |


## # Environment Variables in Docker and Kubernetes

## Docker Image Environment Variables

The Docker images used in this project do **not** have any environment variables hardcoded inside the Dockerfile. This design choice ensures that the images remain portable, reusable, and environment-agnostic.

## Injecting Environment Variables at Runtime

Instead of embedding environment variables within the image, we inject them dynamically when the containers are deployed on Kubernetes. This is done by using:

- **Kubernetes Secrets** for sensitive data (e.g., API keys, database passwords).
- **Kubernetes ConfigMaps** for non-sensitive configuration data.

These Kubernetes resources are then referenced in the Deployment manifests and passed as environment variables to the containers.

## Benefits

- **Security:** Sensitive data is not baked into the image but managed securely via Kubernetes Secrets.
- **Portability:** Same image can be deployed across different environments (dev, staging, prod) with different configurations.
- **Flexibility:** Configuration can be updated without rebuilding images by simply modifying the Secrets or ConfigMaps.


## Example: Injecting Environment Variables from a Secret

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: users
  template:
    metadata:
      labels:
        app: users
    spec:
      containers:
        - name: users
          image: users-service:latest
          imagePullPolicy: Never
          envFrom:
            - secretRef:
                name: users-secret
```
Generate `users-secret` using `.env` using the command

```bash
kubectl create secret generic users-secret --from-file=./services/users/.env
```