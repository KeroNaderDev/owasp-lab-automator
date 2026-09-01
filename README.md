# 🧪 OWASP Lab Automator — Demo

Scripts that auto-test OWASP Top 10 on a lab target

> **Cybersecurity Track — Demo Showcase** | **Real Problem, Synthetic Data**

## Overview
**Problem:** OWASP labs require manual repetitive testing

**Solution:** Scripts that auto-test OWASP Top 10 on a lab target This demo proves the engineering approach with synthetic data.

## Architecture
```
Target → Scanner (SQLi/XSS/SSRF) → Reporter → Dashboard
```

## Tech Stack
- Python, OWASP, Docker

## Features
- Auto SQLi/XSS/SSRF checks\n- One-click report\n- Dockerized lab

## Security
- Validation, JWT/RBAC, Rate limiting, No real secrets

## Screenshots
![Demo](./screenshots/demo.png)

## Demo
- **Demo Data:** `demo-data.json`
- **Live:** `https://kero.10001mb.com/demo/owasp-lab-automator-demo` *(placeholder)*

## Installation
```bash
git clone https://github.com/KeroNaderDev/owasp-lab-automator-demo.git
cd owasp-lab-automator-demo
npm install
cp .env.example .env
npm run dev
```

## Usage
```bash
npm run dev
```

## What I Learned
- Cybersecurity end-to-end design
- Demo vs real data separation
- Professional portfolio structure

---
*Track: Cybersecurity • Portfolio: [KeroNaderDev](https://github.com/KeroNaderDev)*
