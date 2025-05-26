## Continuous Integration & Continuous Deployment (CI/CD)

- **Purpose:** Automate building, testing, and deploying applications.
- **Popular Tools:**
  - **GitHub Actions:** Native GitHub automation workflows.
  - **GitLab CI/CD:** Integrated with GitLab repositories.
  - **Jenkins:** Highly customizable automation server.
  - **CircleCI, Travis CI:** Cloud-based pipelines.
- **Why Use CI/CD?**
  - Faster and reliable software delivery.
  - Catch bugs early with automated tests.
  - Consistent deployment environments.
- **How it Fits:** Connects source code repos with Kubernetes deployments and Terraform infrastructure.


## ELK Stack (Elasticsearch, Logstash, Kibana)

- **Purpose:** Centralized logging, searching, and visualization of application and infrastructure logs.
- **Components:**
  - **Elasticsearch:** Distributed search and analytics engine.
  - **Logstash:** Data processing pipeline (collect, transform, ship logs).
  - **Kibana:** Visualization dashboard for logs and metrics.
- **Why Use ELK?**
  - Easier troubleshooting and root cause analysis.
  - Monitor app health and performance.
  - Correlate logs across microservices and infrastructure.
- **Integration:** Works alongside Prometheus and Grafana to provide comprehensive observability.
