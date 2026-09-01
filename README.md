# owasp-lab-automator-demo

🧪 OWASP Lab Automator — Demo | Automates OWASP Top 10 tests

> **Demo Showcase — Synthetic Data Only** — No personal data used.

## Overview
Demo project that solves a real problem in **Cybersecurity** track. Built as a portfolio showcase with synthetic demo data.

## Architecture
```
Client → Secure Gateway → Backend API → Database
        ↓
   Security Layer (OWASP, Validation, Rate Limit)
```

## Tech Stack
- **Track:** Cybersecurity
- See `package.json` / `requirements.txt` for full list

## Features
- Solves real problem with demo data
- Secure by design (validation, auth, RBAC where applicable)
- Production-ready structure

## Security
- Input validation
- Authentication & Authorization (JWT/RBAC)
- API security best practices
- No real secrets — demo only

## Screenshots
![Demo Screenshot](./screenshots/demo.png)
*Placeholder — add real screenshot*

## Demo
Demo data: `demo-data.json` (synthetic)
Live Demo: `https://kero.10001mb.com/demo/owasp-lab-automator-demo` (placeholder)

## Installation
```bash
git clone https://github.com/KeroNaderDev/owasp-lab-automator-demo.git
cd owasp-lab-automator-demo
npm install # or pip install -r requirements.txt
cp .env.example .env
npm run dev
```

## Usage
```bash
npm run dev
# Open http://localhost:3000
```

## What I Learned
- Building Cybersecurity systems end-to-end
- Securing APIs and infrastructure
- Demo-driven portfolio design

---
*Part of **Kero Nader** — Cybersecurity | Full Stack | DevOps | IoT — Track: Cybersecurity*
