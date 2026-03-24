# 👁️ Third EYE – AI Driven SOC Platform

## 🚀 Overview
Third EYE is an AI-powered Security Operations Center (SOC) platform integrating SIEM and SOAR to automate detection, analysis, and response.

## 🧠 Features

- 🔍 AI-based incident analysis and decision-making
- ⚡ Automated response (Block / Monitor / Escalate)
- 🧬 UEBA (User Behavior Analytics) for anomaly detection
- 🛡️ Threat Intelligence integration
- 🗺️ MITRE ATT&CK mapping
- 🔎 AI-powered threat hunting
- 🌐 Dark web monitoring (extensible)
- 📊 Role-based SOC dashboard (L1 / L2 / Admin)
- ☁️ SaaS multi-tenant ready architecture
- 🎤 Voice command support (experimental)

## 🏗️ Architecture
  Endpoints → SIEM → AI Engine → SOAR → Action → Dashboard
## 🖥️ System Architecture

### 1. AI Server
- Runs AI engine and backend APIs
- Handles analysis and decision-making

### 2. SIEM Platform
- Provides security events and offenses

### 3. SOAR Platform
- Executes automated response playbooks

### 4. Dashboard Server
- Displays incidents and AI decisions

---
▶️ Running the Project
## Start Backend API
uvicorn backend.app:app --reload
## Start Dashboard
streamlit run frontend/dashboard.py
## Run SOAR Playbook (Optional)
python integrations/soar_playbook.py

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/Third-EYE-AI-SOC.git
cd Third-EYE-AI-SOC
pip install -r requirements.txt


## 🔐 Configuration
Edit backend/config.py
QRADAR_IP = "https://your-qradar-ip"
QRADAR_TOKEN = "your-token"
VT_API = "your-api-key"

## ⚠️ Disclaimer
For educational use. Validate before production.

## 👨‍💻 Author
Rohit
