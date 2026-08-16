# Deployment Guide

## Local demo

```bash
cd working_demo
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Docker

```bash
cd working_demo
docker compose up --build
```

## Render

The working demo includes `working_demo/render.yaml` for Docker deployment. Connect the GitHub repository to Render and select the `working_demo` directory as the service root, or create a Docker web service using `working_demo/Dockerfile` and expose port 8000.

## AWS reference implementation

The Terraform directory is intentionally a reference architecture rather than an automatic production deployment. Before applying it to AWS, review CIDRs, routes, IAM permissions, region, availability zones, and cost implications.

Never commit real credentials or secrets. Use an AWS profile, IAM role, or another secure credential mechanism.
