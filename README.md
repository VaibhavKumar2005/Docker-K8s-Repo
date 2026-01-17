# ☸️ Docker & Kubernetes Learning Journey

This repository documents my hands-on experiments with Cloud Native technologies, focusing on **Docker containerization** and **Kubernetes orchestration**.

## 🚀 Projects

### 1. Project Hydra (High Availability Nginx)
**Goal:** Demonstrate Kubernetes' "Self-Healing" capabilities and Load Balancing.

* **Architecture:**
    * **Deployment:** 3 Replicas of Nginx (Alpine version).
    * **Service:** Type LoadBalancer to expose the application.
    * **Orchestrator:** Minikube (running on Docker driver).

* **Key Concepts Applied:**
    * **ReplicaSets:** Ensuring 3 pods are always running (Self-Healing).
    * **Declarative YAML:** Defining infrastructure as code.
    * **Services:** Stable networking and traffic distribution.

#### 🛠️ How to Run
\\\ash
# 1. Start the Cluster
minikube start

# 2. Deploy the Hydra (3 Heads)
kubectl apply -f hydra.yaml

# 3. Create the Service (The Receptionist)
kubectl apply -f service.yaml

# 4. Access the App
minikube service echo-service
\\\

## 📂 Repository Structure
\\\
.
├── Docker/             # Dockerfiles and Source Code
└── K8s/                # Kubernetes Manifests (YAML)
    ├── hydra.yaml      # Deployment Manifest
    └── service.yaml    # Service Manifest
\\\

---
*Created by Vaibhav Kumar | Learning DevOps, One Pod at a Time.*
