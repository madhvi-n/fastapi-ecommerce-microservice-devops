# 🗭 Helm

## 🔧 What is Helm?

Helm is the **package manager for Kubernetes**. It simplifies the deployment and management of Kubernetes applications using reusable, versioned templates called **charts**.

* Think of Helm charts like Docker images but for Kubernetes apps
* Manages Kubernetes manifests as version-controlled templates
* Supports variables, reusability, upgrades, and rollbacks


## 🧠 Key Concepts Used in This Project

* **Chart**: A Helm package containing templates and default configuration values.
* **Release**: An instance of a Helm chart running in a Kubernetes cluster.
* **Values file**: YAML file that supplies configuration values to templates.
* **Templates**: Go-based templates rendered into Kubernetes manifests.


## 🚀 Why Use Helm?

* 🧩 Modular and reusable YAML configs
* 🔄 Rollback and versioning support
* ⚙️ Configurable per environment via `values.yaml`
* 📦 Easily share apps via Helm repositories
* 🧪 Great fit for GitOps, CI/CD pipelines


## 🏗 How We Use Helm in This Project

* Create Helm charts for each microservice (`users`, `products`, `nginx`)
* Define deployment and service templates with variables
* Store configuration (e.g., image names, env, ports) in `values.yaml`
* Use `helm install` or `helm upgrade` for deployments
* Package and reuse charts across environments (dev, staging, prod)


## 🧱 Key Helm Components

### 1. **Chart**

* Directory with templates, values, and metadata (like a mini-package)
* Standard files:

  * `Chart.yaml` – chart metadata
  * `values.yaml` – default configuration
  * `templates/` – Kubernetes YAML templates

### 2. **Release**

* A running instance of a chart in a Kubernetes cluster
* Can have multiple releases from the same chart (e.g., `users-dev`, `users-prod`)

### 3. **Values**

* Configuration input passed to templates
* Overrides default values using `--values` or `--set`

### 4. **Templates**

* YAML files using Go templating language (`{{ .Values.image.repository }}`)
* Supports logic, loops, conditionals for dynamic manifest generation


## 🔁 Helm Workflow

1. Scaffold chart using:

   ```bash
   helm create <chart-name>
   ```

2. Customize templates and `values.yaml`

3. Install chart:

   ```bash
   helm install <release-name> ./<chart-name>
   ```

4. Upgrade with new config or template changes:

   ```bash
   helm upgrade <release-name> ./<chart-name>
   ```

5. Delete a release:

   ```bash
   helm uninstall <release-name>
   ```

6. Package and share:

   ```bash
   helm package <chart-folder>
   helm repo add <name> <url>
   ```


## 🔍 Basic Helm Commands

```bash
# Create a new chart
helm create my-app

# Install a release
helm install my-app ./my-app

# Upgrade a release
helm upgrade my-app ./my-app

# List all releases
helm list

# View a release’s status
helm status my-app

# Uninstall a release
helm uninstall my-app

# Lint chart for errors
helm lint ./my-app

# Dry run without applying
helm install my-app ./my-app --dry-run

# Use a custom values file
helm install my-app ./my-app -f custom-values.yaml
```


## 📚 Further Reading

* [Helm Official Docs](https://helm.sh/docs/)
* [ArtifactHub](https://artifacthub.io/) – Browse and reuse public Helm charts
* [Helm Charts Best Practices](https://helm.sh/docs/chart_best_practices/)
