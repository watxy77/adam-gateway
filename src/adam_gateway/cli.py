"""
Adam Gateway CLI Entry Point.

Provides command-line interface for managing the gateway.
"""

import click
import uvicorn

from adam_gateway.config import get_settings


@click.group()
@click.version_option(version="0.1.0")
def main():
    """Adam Gateway - LLM API Gateway CLI."""
    pass


@main.command()
@click.option("--host", default=None, help="Server host")
@click.option("--port", default=None, type=int, help="Server port")
@click.option("--workers", default=None, type=int, help="Number of workers")
@click.option("--reload", is_flag=True, help="Enable auto-reload")
def serve(host: str | None, port: int | None, workers: int | None, reload: bool):
    """Start the Adam Gateway server."""
    settings = get_settings()

    uvicorn.run(
        "adam_gateway.main:app",
        host=host or settings.host,
        port=port or settings.port,
        workers=workers or settings.workers,
        reload=reload,
        log_level=settings.log_level.lower(),
    )


if __name__ == "__main__":
    main()
