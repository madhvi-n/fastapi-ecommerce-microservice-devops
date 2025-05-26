# 🚪 Kubernetes Ingress Setup Guide for Microservices

This guide explains how to configure **Ingress** in a Minikube-based Kubernetes cluster to enable clean routing for your microservices (e.g., `users`, `products`).


## ✅ Prerequisites

- Minikube installed and running.
- Services (`users`, `products`, etc.) already deployed via Helm.
- Docker images already built and used in Helm deployments.


## 🔌 Step 1: Enable Ingress Controller in Minikube

Run the following command to enable NGINX Ingress:

```bash
minikube addons enable ingress
```

## 🧭 Step 2: Update Local DNS (/etc/hosts)
To access services via a domain like app.local, add this line to your local /etc/hosts file:

```bash
127.0.0.1 app.local
```

Note:
- On Linux/macOS: Use sudo nano /etc/hosts
- On Windows: Edit C:\Windows\System32\drivers\etc\hosts as administrator.

## 🛠️ Step 3: Create the Ingress Resource
Create a file named ingress.yaml with the following content:

```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
    - host: app.local
      http:
        paths:
          - pathType: Prefix
            path: /users(/|$)(.*)
            backend:
              service:
                name: users-service
                port:
                  number: 80
          - pathType: Prefix
            path: /products(/|$)(.*)
            backend:
              service:
                name: products-service
                port:
                  number: 80

```
Make sure the `service.name` values match your deployed service names.

## 🚀 Step 4: Apply the Ingress Configuration
Run
```bash
kubectl apply -f ingress.yaml
kubectl get ingress
```

## 🌐 Step 5: Access the Microservices
Open your browser or use `curl`:
* `http://app.local/users`
* `http://app.local/products`

## Step 6 : Clean Up
To remove the ingress resource:


```bash
kubectl delete ingress app-ingress
```