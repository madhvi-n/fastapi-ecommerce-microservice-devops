# 🚪 Kubernetes Ingress Setup Guide for Microservices

This guide explains how to configure **Ingress** in a Minikube-based Kubernetes cluster to enable clean routing for your microservices (e.g., `users`, `products`).


## ✅ Prerequisites

* Minikube installed and running.
* NGINX Ingress addon enabled.
* Microservices (e.g., users, products) deployed via **Helm**, using local **Docker** images.
* Services should be running and exposing HTTP ports (e.g., 8000).



## 🔌 Step 1: Enable Ingress Controller in Minikube

This adds the NGINX ingress controller under the ingress-nginx namespace.
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
          - pathType: ImplementationSpecific
            path: /users(/|$)(.*)
            backend:
              service:
                name: users-service
                port:
                  number: 8000
          - pathType: ImplementationSpecific
            path: /products(/|$)(.*)
            backend:
              service:
                name: products-service
                port:
                  number: 8000

```
⚠️ Important Notes:

- Ensure `service.name` exactly matches the name of the service deployed by Helm. You can confirm via:
```bash
kubectl get svc
```
- Match the correct exposed port (e.g., 8000 if your app listens on that).
- Do not use regex-like paths such as `/users(/|$)(.*)` with `pathType: Prefix`. Instead, use `pathType: ImplementationSpecific`.

## 🚀 Step 4: Apply the Ingress Configuration
Run
```bash
kubectl apply -f ingress.yaml
kubectl get ingress
```
If you see a 503 error later, verify that the service name and port are correct.



## 🌐 Step 5: Access the Microservices
Now test the routing:
#### Option 1. Browser

* `http://app.local/users`
* `http://app.local/products`


#### Option 2:  Curl
```bash
curl -H "Host: app.local" http://$(minikube ip)/users/health
curl -H "Host: app.local" http://$(minikube ip)/products/health
```


## Step 6 : Clean Up
To remove the ingress resource:


```bash
kubectl delete ingress app-ingress
```

## 📝 Troubleshooting & Common Errors
| Issue                           | Cause                                       | Fix                                                   |
|---------------------------------|---------------------------------------------|--------------------------------------------------------|
| 503 Service Temporarily Unavailable | Ingress can't find the service             | Ensure `service.name` and `port.number` are correct   |
| Error obtaining Endpoints...   | Wrong `service.name` in `ingress.yaml`      | Use `kubectl get svc` to find the actual service names|
| DNS not resolving `app.local`  | Missing `/etc/hosts` entry                  | Add `127.0.0.1 app.local` to your hosts file          |
| Path regex not accepted        | Using `/path(/|$)(.*)` with `pathType: Prefix` | Use `pathType: ImplementationSpecific` instead        |