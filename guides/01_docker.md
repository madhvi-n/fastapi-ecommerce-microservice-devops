# 🐳 Docker Guide

## 🔧 What is Docker?
Docker is a tool that lets you **package apps into containers** so they run the same everywhere—on your laptop, server, or cloud.

- Containers include your code, libraries, and dependencies
- Solves the “it works on my machine” problem
- Lightweight and fast compared to virtual machines

## 🧩 Core Concepts You’ll Use
- Image: A snapshot of your app with everything it needs to run
- Container: A running instance of an image
- Dockerfile: Script that tells Docker how to build your image
- Volume: Maps folders between your machine and the container (for data)
- Network: Allows containers to talk to each other
- Docker Compose: Tool for defining and running multi-container apps

## 💡 Why Use Docker?
- Run apps consistently across environments
- Package everything needed into one container
- Isolate apps for better security
- Great for microservices and DevOps workflows
- Easy to test, ship, and scale applications

## 🧱 How We Use Docker in This Project?
- Each service (users, products) has its own Dockerfile
- Docker Compose is used for local multi-container development
- Environment variables are passed using .env files or Compose files
- Images are either:
    - Loaded into Minikube for Kubernetes
    - Pushed to Docker Hub or another registry for deployment

## ⚙️ Common Docker Components
1. Image
    - Read-only template
    - Built from a Dockerfile
    - Examples: python:3.11, ubuntu, myapp:latest

2. Container
    - A running app built from an image
    - Lightweight and isolated

3. Dockerfile
    - A text file with step-by-step build instructions
    - Used to create your custom image

4. Volume
    - Keeps data even if the container is deleted
    - Mounts folders between your host and container

5. Network
    - Lets containers talk to each other using service names
    - Compose sets up a default network automatically

6. Docker Compose
    - Defines how multiple containers work together
    - Uses `docker-compose.yml` for configuration

## 🔁 Docker Workflow
- Write a `Dockerfile` for each service
- Build an image using `docker build`
- Run it using `docker run`
- For multiple services, create a `docker-compose.yml`
- Use `docker-compose up` to run all services
- Debug using `logs, exec, inspect`, etc.


## 🧪 Useful Docker & Compose Commands
```bash
# Build and run
docker build -t myapp:latest .
docker run -p 8000:80 myapp:latest

# View running containers
docker ps

# Stop or remove
docker stop <container-id>
docker rm <container-id>

# View images
docker images
docker rmi <image-id>

# Execute a command inside a container
docker exec -it <container-id> bash

# Use Docker Compose
docker-compose up --build
docker-compose down

# Build with Compose
docker-compose build

# Logs
docker logs <container-id>
```


## 📚 Learn More

* [Docker Official Docs](https://docs.docker.com/)
* [Play With Docker (interactive)](https://labs.play-with-docker.com/)
* [Docker Compose Docs](https://docs.docker.com/compose/)
* [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
