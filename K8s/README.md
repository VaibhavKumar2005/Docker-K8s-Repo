# ☸️ Docker & Kubernetes Learning Journey

This repository documents my hands-on experiments with Cloud Native technologies, focusing on **Docker containerization** and **Kubernetes orchestration**.

## 🚀 Projects

### 0. Docker Basics (Containerization)
**Goal:** Package a legacy application into a portable container.
* **Base Image:** Alpine Linux (Lightweight).
* **Key Commands:** \docker build\, \docker run\, \docker push\.
* **Outcome:** Created a custom image \aibhavkumar0412/my-ml-project\ capable of running on any machine.

### 1. Project Hydra (High Availability K8s)
**Goal:** Demonstrate Kubernetes' "Self-Healing" capabilities and Load Balancing.

* **Architecture:**
    * **Deployment:** 3 Replicas of Nginx.
    * **Service:** Type LoadBalancer to expose the application.
    * **Orchestrator:** Minikube.

* **Key Concepts Applied:**
    * **ReplicaSets:** Ensuring 3 pods are always running.
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
