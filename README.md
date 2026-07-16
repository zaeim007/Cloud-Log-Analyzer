# Cloud Log Analyzer

A cloud-based log monitoring and security analysis platform that analyzes server log files, detects security threats, and visualizes insights through an interactive dashboard.
The application is containerized using Docker, deployed on AWS EC2 behind Nginx and Gunicorn, and automatically deployed using GitHub Actions CI/CD.

## Features

- Upload `.log` and `.txt` files
- Log parsing with O(n) single-pass processing
- Error rate and status code analysis
- Top IP and page analytics
- Suspicious IP detection
- Brute-force attack detection
- Excessive 404 scanner detection
- Interactive dashboard with Chart.js
- Dockerized deployment
- Automated CI/CD with GitHub Actions

---

## Tech Stack

**Backend**
- Python
- Flask

**Frontend**
- HTML
- CSS
- Chart.js

**Cloud & DevOps**
- AWS EC2
- Docker
- Docker Compose
- Gunicorn
- Nginx
- GitHub Actions

---

## Architecture

```
Developer
    │
 git push
    │
    ▼
  GitHub
    │
GitHub Actions
    │
   SSH
    ▼
 AWS EC2
    │
Docker Compose
    │
 Gunicorn
    │
  Flask
    │
  Nginx
    ▼
 Browser
```

---

## Run Locally

```bash
git clone https://github.com/zaeim007/Cloud-Log-Analyzer.git

cd Cloud-Log-Analyzer

pip install -r requirements.txt

python app.py
```

### Run with Docker

```bash
docker compose up --build -d
```

---

## Deployment

The application is deployed on **AWS EC2** using:

- Docker
- Docker Compose
- Gunicorn
- Nginx
- GitHub Actions (CI/CD)

Every push to the **main** branch automatically deploys the latest version to the EC2 server.

---

## Project Highlights

- Cloud-based log analysis
- Statistical security detection
- Professional dashboard
- Dockerized application
- AWS deployment
- Automated CI/CD pipeline
