# Ecommerce-fastapi
A scalable e-commerce backend built with FastAPI, designed with a microservices architecture. Each service runs in its own Docker container, managed via Docker Compose, and ready for Kubernetes deployment. Terraform will be added for infrastructure as code.


## Features
- Microservices architecture with independent services for users, products, and more
- Authentication with OAuth (Google, GitHub)
- Role-based access control (Admin, Staff, Customer roles)
- PostgreSQL or SQLite database support via SQLAlchemy ORM
- JWT token authentication
- Dockerized services for consistent environments
- Kubernetes manifests for container orchestration (coming soon)
- Terraform integration for cloud infrastructure (planned)

## Getting Started

### Prerequisites

- Docker & Docker Compose installed ([Get Docker](https://docs.docker.com/get-docker/))
- Python 3.11+ (for local dev)
- (Optional) Kubernetes cluster (e.g., Minikube, kind) for deployment
- (Optional) Terraform CLI for infrastructure automation


### Running Locally with Docker Compose

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/ecommerce-fastapi.git
   cd ecommerce-fastapi
   ```

2. Create .env files for each service under services/users/ and services/products/ with necessary environment variables (e.g., DATABASE_URL, GOOGLE_CLIENT_ID, etc.) Refer to `.env.example`

3. Build and start the services:
    ```bash
    docker compose up --build
    ```

4. Access the apis:
    - Users service: http://localhost:8001/docs
    - Products service: http://localhost:8002/docs

5. To stop the services
    ```bash
    docker compose down
    ```

### Running Locally without Docker (for dev/testing)
You can also run each service individually using Uvicorn inside their folder:
    ```bash
    cd services/users
    pip install -r requirements.txt
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

## Next Steps
- Add Kubernetes manifests to k8s/ folder for deploying services to a cluster
- Add Terraform scripts in terraform/ to provision infrastructure (cloud DB, cluster, networking)
- Add CI/CD pipeline to automate build, test, and deployment
- Implement additional services (orders, payments, etc.)
