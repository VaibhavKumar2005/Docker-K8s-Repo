# ☸️ Cloud Native Learning Journey: Docker & Kubernetes

This repository documents my hands-on journey mastering Cloud Native engineering, moving from basic containerization to self-healing distributed systems.

## 📂 Repository Structure

### 📁 1. Docker/ (Containerization)
* **Goal:** Package legacy Python applications into portable Alpine-based containers.
* **Tech Stack:** Python, Docker, Alpine Linux.
* **Key Achievement:** Reduced image size and implemented multi-stage builds.

### 📁 2. K8s/ (Orchestration & Security)
* **Project Hydra:** A High-Availability Nginx deployment.
* **Architecture:**
    * **Self-Healing:** 3 Replicas managed by a Deployment controller.
    * **Decoupled Config:** HTML injected via **ConfigMaps** (No image rebuilds).
    * **Security:** API Keys injected via **Kubernetes Secrets** (No hardcoded credentials).
    * **Networking:** Exposed via LoadBalancer Service.

## 🛠️ How to Run Project Hydra

1. **Start Minikube:** `minikube start`
2. **Create Secret Vault:** `kubectl create secret generic ai-keys --from-literal=api_key=sk-fake-123`
3. **Deploy:**
   ```bash
   cd K8s
   kubectl apply -f configmap.yaml
   kubectl apply -f deployment.yaml 
