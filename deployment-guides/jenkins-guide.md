# Jenkins Deployment Guide for Kubernetes Microservices Project

This guide covers how to deploy Jenkins in a Docker container for building, loading, and deploying your microservices with Docker, Minikube, Helm, and kubectl.

---

## Prerequisites

- Docker installed and running on your local machine.
- Minikube cluster up and running.
- Docker CLI, Helm, kubectl, and Minikube CLIs installed on your host machine.
- Project files organized with microservices in `services/` and Helm charts in `helm-charts/`.


## Step 1: Prepare Docker-Compose for Jenkins

Create or update `docker-compose.jenkins.yml` in your project root with the following content:

```yaml
version: '3'
services:
  jenkins:
    image: jenkins/jenkins:lts
    ports:
      - 8080:8080
      - 50000:50000
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
      - /usr/bin/docker:/usr/bin/docker
      - /usr/local/bin/helm:/usr/local/bin/helm
      - /usr/local/bin/kubectl:/usr/local/bin/kubectl
      - /usr/local/bin/minikube:/usr/local/bin/minikube

volumes:
  jenkins_home:
```

## Step 2: Start Jenkins Container
Run Jenkins with Docker Compose:
```bash
docker-compose -f docker-compose.jenkins.yml up -d
```
Verify Jenkins container is running:

```bash
docker ps
```

## Step 3: Access Jenkins UI
Open your browser and navigate to:
```bash
http://localhost:8080
```

Follow the Jenkins setup wizard to unlock Jenkins (retrieve initial admin password from the container logs or `/var/jenkins_home/secrets/initialAdminPassword`).

## Step 4: Verify CLI Tools Inside Jenkins Container
Exec into the Jenkins container shell
```bash
docker exec -it ecommerce-fastapi_jenkins_1 bash
```

Check installed tools
```sh
docker --version
helm version
kubectl version --client
minikube version
```
If any CLI is missing, verify the volume mounts in your compose file.


## Step 5: Configure Jenkins for Your Pipeline
* Install necessary Jenkins plugins:
    - Docker Pipeline
    - Kubernetes CLI Plugin
    - Pipeline
* Create your Jenkins Pipeline job using a Jenkinsfile in your project root.

## Step 6: Run Your Pipeline
The pipeline will:

* Build Docker images for microservices.
* Load Docker images into Minikube’s Docker daemon.
* Deploy or upgrade Helm releases.

## Step 7: Clean Up
To stop and remove the Jenkins container and volume:
```sh
docker-compose -f docker-compose.jenkins.yml down -v
```


## Tips & Troubleshooting
* Ensure Docker daemon on your host is running before starting Jenkins.
* If Jenkins can’t find Docker or Helm, double-check your binary mounts.
* Minikube's Docker environment should not be overridden inside Jenkins container; Jenkins uses host Docker daemon.
* For DNS resolution issues, ensure your `/etc/hosts` is correctly set (e.g., mapping `app.local` to `127.0.0.1`).
* If ports 8080 or 50000 are occupied, adjust ports in your docker-compose file.