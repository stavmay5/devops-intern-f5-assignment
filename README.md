# F5 DevOps Intern Assignment

This repository contains my solution for the F5 DevOps Intern Home Assignment.
The project demonstrates a containerized Nginx web server environment with an automated testing suite, orchestrated via Docker Compose and validated through a GitHub Actions CI pipeline.

## Features

### Core Requirements
- **Web Server:** Custom Nginx container serving a welcome page on port `8080` (HTTP 200).
- **Error Simulation:** Simulated internal server error on port `8081` (HTTP 500).
- **Automated Testing:** A separate Python container that validates endpoints and logic.
- **Orchestration:** `docker-compose.yml` to run the server and tester in a shared network.
- **CI/CD:** GitHub Actions pipeline that builds, tests, and uploads result artifacts (`succeeded.txt` / `fail.txt`).

### Bonus Implementation: Rate Limiting
As requested in the advanced requirements, I implemented traffic shaping to protect the server:
- **Nginx Configuration:** Configured `limit_req_zone` to restrict clients to **5 requests per second** (with a small burst allowance).
- **Validation:** The test script includes a specific "Stress Test" that fires 20 rapid requests to verify that the server correctly returns `503 Service Unavailable` when the limit is exceeded.

## Technologies
- **Docker & Docker Compose**
- **Nginx** (Alpine based for minimal footprint)
- **Python 3.9** (Slim image for optimization)
- **GitHub Actions** (CI Automation)

## Project Structure

```text
├── nginx/
│   ├── Dockerfile         # Nginx image configuration
│   ├── nginx.conf         # Server config (Ports + Rate Limiting)
│   └── index.html         # Custom entry page
├── tester/
│   ├── Dockerfile         # Python tester image configuration
│   └── test_script.py     # Logic for HTTP checks & Stress testing
├── .github/workflows/
│   └── ci.yml             # CI Pipeline definition
├── docker-compose.yml     # Orchestration file
└── README.md              # Project documentation