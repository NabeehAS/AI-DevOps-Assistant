# AI DevOps Assistant

**An intelligent DevOps assistant API built with FastAPI, Docker, and modern CI/CD practices**

## Overview
This project demonstrates a production-ready DevOps workflow using:
- **FastAPI** for building a high-performance REST API
- **Docker** for containerization
- **GitHub Actions** for CI/CD automation
- **Infrastructure as Code** principles

Perfect for showcasing DevOps skills required for junior positions in the Israeli tech market.

## Project Structure
```
AI-DevOps-Assistant/
├── app/
│   ├── __init__.py          # Package initializer
│   └── main.py              # FastAPI application
├── tests/
│   ├── __init__.py          # Tests package initializer
│   └── test_main.py         # API endpoint tests
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
├── Dockerfile               # Container configuration
├── docker-compose.yml       # Local development setup
├── requirements.txt         # Python dependencies
├── .dockerignore           # Docker build exclusions
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Features
- RESTful API with FastAPI
- Health check endpoints for monitoring
- Docker containerization with optimized builds
- Automated CI/CD pipeline with GitHub Actions
- Comprehensive test suite with pytest
- Environment-based configuration
- Production-ready structure with best practices

## Quick Start

### Local Development (Python)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload --port 8000

# Visit http://localhost:8000
# API docs available at http://localhost:8000/docs

# Run tests
pytest tests/ -v
```

### Docker Development
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build and run manually
docker build -t ai-devops-assistant .
docker run -p 8000:8000 ai-devops-assistant

# Visit http://localhost:8000
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint with welcome message |
| `/health` | GET | Health check for monitoring |
| `/api/v1/info` | GET | API version and environment info |
| `/docs` | GET | Interactive API documentation (Swagger UI) |
| `/redoc` | GET | Alternative API documentation (ReDoc) |

## Development Workflow

1. **Make changes** to the code in `app/` directory
2. **Test locally** using `uvicorn` or `docker-compose`
3. **Commit changes** to Git
4. **Push to GitHub** - triggers CI/CD pipeline
5. **Pipeline runs** linting, tests, and builds Docker image
6. **Review results** in GitHub Actions tab

## Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Key variables:
- `ENVIRONMENT`: development/staging/production
- `API_PORT`: Port to run the service (default: 8000)

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) automatically:
- Runs on every push/PR to main or develop branches
- Lints code with flake8
- Runs tests with pytest
- Builds Docker image
- Tests the containerized application

## Next Steps

This base setup is ready for expansion:
- [ ] Add database integration (PostgreSQL/MongoDB)
- [ ] Implement authentication & authorization
- [ ] Expand test coverage
- [ ] Set up Kubernetes deployment files
- [ ] Create Terraform/IaC for cloud infrastructure
- [ ] Add monitoring & logging (Prometheus, Grafana)
- [ ] Implement AI/ML features

## Technology Stack

- **Language**: Python 3.11
- **Framework**: FastAPI 0.115+
- **Server**: Uvicorn
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Future**: Kubernetes, Terraform, AWS/Azure

## Contributing

1. Create a feature branch
2. Make your changes
3. Ensure tests pass
4. Submit a pull request

## License

MIT License - feel free to use this project for learning and portfolio purposes.
