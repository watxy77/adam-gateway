"""
Adam Gateway - Main Application Entry Point.

A production-ready LLM API Gateway with intelligent routing,
multi-provider support, and enterprise-grade security.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger
import sys

from adam_gateway.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Startup
    settings = get_settings()
    logger.info(f"Starting Adam Gateway v0.1.0")
    logger.info(f"Server: {settings.host}:{settings.port}")
    logger.info(f"Log level: {settings.log_level}")
    yield
    # Shutdown
    logger.info("Shutting down Adam Gateway")


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title="Adam Gateway",
        description="A production-ready LLM API Gateway",
        version="0.1.0",
        lifespan=lifespan,
    )

    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy", "version": "0.1.0"}

    @app.get("/")
    async def root():
        """Root endpoint."""
        return {
            "name": "Adam Gateway",
            "version": "0.1.0",
            "docs": "/docs",
        }

    return app


app = create_app()
