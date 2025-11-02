# AI DevOps Assistant 

**Short:** Demo FastAPI service to showcase containerization, CI and a deployment-ready skeleton for a DevOps + AI portfolio project.

## What is this
Small backend service used as a foundation for an AI-powered DevOps assistant project. This repo contains:
- FastAPI app
- Dockerfile for containerization
- GitHub Actions CI workflow: tests + build

## Quickstart (local)
```bash
# create venv
python3 -m venv .venv
source .venv/bin/activate

# install
pip install -r requirements.txt

# run locally
uvicorn app.main:app --reload --port 8000
