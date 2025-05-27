# 🗄 Jenkins
## 🔧 What is Jenkins?
Jenkins is a popular open-source automation server used to implement Continuous Integration (CI) and Continuous Deployment (CD) workflows.
* It automates repetitive development tasks like building, testing, and deploying software.
* Helps maintain code quality by automating builds and tests
* Supports plugins to integrate with Docker, Kubernetes, Helm, Git, and many other tools
* Enables fast feedback loops and repeatable deployments


## 🧠 Key Concepts Used in This Project
**Pipeline**: A set of automated stages that define your build and deploy process, usually described in a Jenkinsfile
**Agent**: The environment where Jenkins executes pipeline steps (e.g., Docker container, local machine)
**Stages**: Logical steps in a pipeline such as Build, Test, Deploy
**Jobs**: Configured units of work that run pipelines or individual build steps
**Plugins**: Extend Jenkins functionality (e.g., Docker plugin, Kubernetes plugin)

## 🚀 Why Use Jenkins?
* 🔄 Automate building, testing, and deployment pipelines
* 🧩 Integrate easily with Docker and Kubernetes workflows
* 📈 Reduce manual errors and accelerate delivery
* 🤝 Support for multi-service microservices projects via pipelines
* 🔐 Centralized control and logs of all automation tasks

## 🏗 How We Use Jenkins in This Project
Build Docker images for each microservice (`users, products`)
Load built images into Minikube's Docker environment
Deploy microservices on Kubernetes clusters using Helm charts
Automate this entire workflow in a Jenkins Pipeline (`Jenkinsfile`)
Run Jenkins itself inside a Docker container for easy setup

## Jenkins Job vs Agent
| Concept   | Description                                                                                                                      | In Our Project                                                                                |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Job**   | A Jenkins job (or project) defines **what** to execute — such as a pipeline for CI/CD. Think of it as the *script* Jenkins runs. | We'll create a **Pipeline Job** that builds Docker images and deploys them to Kubernetes.     |
| **Agent** | An agent is **where** the job runs — the execution environment (local, Docker, remote server, Kubernetes pod, etc.)              | Our agent will be the **Jenkins Docker container**, using the host Docker via mounted socket. |



## 🧱 Key Jenkins Components in This Project

1. Jenkins Server
- Runs as a Docker container
- Hosts the UI and manages pipeline executions

2. Docker in Docker / Docker Socket
- Jenkins container uses host Docker daemon via mounted socket (/var/run/docker.sock)
- Enables Jenkins to build images and run Docker commands

3. Pipeline (Jenkinsfile)
- Defines multi-stage build and deploy process as code
- Stored in project root for version control

## 🔁 Jenkins Workflow in Our Project
* Start Jenkins server via Docker Compose
* Access Jenkins UI at http://localhost:8080
* Create pipeline jobs or multi-branch pipelines pointing to your Git repo
* Jenkins builds Docker images for microservices
* Load images into Minikube’s Docker environment
* Deploy microservices with Helm charts
* Monitor logs and status in Jenkins UI

## 🔍 Useful Jenkins Commands (Inside Jenkins Container)
```sh
# Access Jenkins container shell
docker exec -it ecommerce-fastapi_jenkins_1 /bin/bash

# Verify Docker CLI
docker --version

# Verify Helm CLI
helm version
```

## 📚 Further Reading
- Jenkins Official Documentation
- Jenkins Pipeline Syntax
- Using Jenkins with Docker
- Helm + Jenkins Integration
