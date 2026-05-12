# Adam Gateway

> A production-ready LLM API Gateway with intelligent routing, multi-provider support, and enterprise-grade security.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![GitHub Stars](https://img.shields.io/github/stars/watxy77/adam-gateway.svg?style=social&label=Star)](https://github.com/watxy77/adam-gateway)

## Features

- **Multi-Protocol Support**: OpenAI, Claude, Gemini, and more
- **Intelligent Routing**: Weighted random, session stickiness, failover
- **Security First**: Prompt Guard, PII detection, content moderation
- **Smart Caching**: Exact match + semantic caching
- **Usage Tracking**: Token counting, billing, quota management
- **High Performance**: Built with FastAPI and async I/O
- **Easy Deployment**: Docker support, single binary deployment

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/watxy77/adam-gateway.git
cd adam-gateway

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -e ".[dev]"
```

### Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit configuration
vim .env
```

### Run

```bash
# Development mode
adam serve --reload

# Production mode
adam serve --host 0.0.0.0 --port 8000 --workers 4
```

## Supported Providers

| Provider | Protocol | Status |
|----------|----------|--------|
| OpenAI | OpenAI Chat/Responses | ✅ |
| Anthropic | Claude Messages | ✅ |
| Google | Gemini Native | ✅ |
| Aliyun | Qwen (OpenAI Compatible) | ✅ |
| Baidu | ERNIE | ✅ |
| Tencent | Hunyuan | ✅ |
| Zhipu | GLM | ✅ |
| DeepSeek | OpenAI Compatible | ✅ |
| Ollama | OpenAI Compatible | ✅ |

## Documentation

- [Getting Started](docs/getting-started.md)
- [Configuration Guide](docs/configuration.md)
- [API Reference](docs/api-reference.md)
- [Deployment Guide](docs/deployment.md)

## Project Structure

```
adam-gateway/
├── src/adam_gateway/     # Main source code
│   ├── adapter/          # Protocol adapters
│   ├── provider/         # Provider configurations
│   ├── service/          # Business services
│   ├── middleware/       # Request middleware
│   ├── storage/          # Data storage
│   ├── scheduler/        # Background tasks
│   ├── prompt/           # Prompt management
│   ├── mcp/              # MCP server support
│   └── utils/            # Utilities
├── tests/                # Test suite
├── docs/                 # Documentation
├── configs/              # Configuration templates
└── scripts/              # Utility scripts
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
