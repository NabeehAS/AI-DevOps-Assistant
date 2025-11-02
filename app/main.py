from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI(
    title="AI DevOps Assistant",
    description="An intelligent DevOps assistant API",
    version="0.1.0"
)

@app.get("/")
def read_root():
    """Root endpoint - health check"""
    return {
        "message": "Welcome to AI DevOps Assistant",
        "status": "running",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "ai-devops-assistant"
    }

@app.get("/api/v1/info")
def get_info():
    """Get API information"""
    return {
        "api_version": "v1",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "endpoints": [
            "/",
            "/health",
            "/api/v1/info"
        ]
    }
