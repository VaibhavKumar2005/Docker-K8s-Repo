🐉 Project Hydra: Unified ML & Sentiment Microservices
<p align="left"> <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" /> <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /> </p>

This repository documents my hands-on journey mastering Cloud Native engineering, moving from basic containerization to self-healing, multi-model distributed systems.

📂 Repository Structure
📁 1. Docker/ (The Application Brain)
Unified API (api.py): A consolidated FastAPI backend that handles both Linear Regression (Score Prediction) and VADER Sentiment Analysis in a single service.

Optimized Environment: Uses a pruned requirements.txt to ensure a lightweight footprint, reducing cold-start latency and attack surface.

Image Versioning: Built and pushed as vaibhavkumar0412/hydra-api:v3-unified.

📁 2. K8s/ (Orchestration & Routing)
Scaling: Backend scaled to 3 Replicas via Deployment manifests for high availability and fault tolerance.

Decoupled Config: The HTML Dashboard and Nginx Reverse Proxy rules are managed via ConfigMaps, allowing for UI updates without rebuilding images.

Modern Deployment: Implements kustomization.yaml to manage all resources as a single, unified stack.

🏗️ Technical Architecture (V3)
Ingress Layer: Nginx acts as the front door, serving the static dashboard from a mounted volume.

Path-Based Routing: Nginx proxies traffic based on the URI:

/predict?hours=X → Routed to the ML logic.

/analyze?text=X → Routed to the Sentiment logic.

Service Discovery: The hydra-api-service provides a stable internal DNS name, load-balancing requests across the three scaled hydra-api pods.

🗺️ Future Roadmap: Gateway API
As the Kubernetes ecosystem transitions from Nginx Ingress to the Gateway API (SIG-Network), the next phase involves:

HTTPRoute Resources: Replacing monolithic Nginx rules with modular, role-oriented routing.

Traffic Management: Implementing weighted splitting for A/B testing new model versions.

🛠️ Deployment Steps
Start the Cluster:

PowerShell
minikube start --memory 4096 --cpus 4
Inject Secrets:

PowerShell
kubectl create secret generic ai-keys --from-literal=api_key=sk-fake-123
Apply All Manifests (The Kustomize Way):

PowerShell
kubectl apply -k K8s/
Launch Dashboard:

PowerShell
minikube service nginx-hydra
