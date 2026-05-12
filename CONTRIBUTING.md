# Contributing to Adam Gateway

Thank you for your interest in contributing to Adam Gateway! This document provides guidelines and information for contributors.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Environment details** (Python version, OS, etc.)
- **Screenshots or logs** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When suggesting an enhancement:

- Use a **clear and descriptive title**
- Provide a **detailed description** of the proposed change
- Explain **why this enhancement would be useful**
- Include **examples** if applicable

### Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Install development dependencies**: `pip install -e ".[dev]"`
3. **Make your changes** following our coding standards
4. **Add tests** for new functionality
5. **Ensure the test suite passes**: `pytest`
6. **Run linting**: `ruff check .` and `ruff format .`
7. **Update documentation** if necessary
8. **Submit your pull request** with a clear description of changes

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/adam-gateway.git
cd adam-gateway

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Coding Standards

### Python Style

- Follow **PEP 8** style guidelines
- Use **type hints** for all function signatures
- Write **docstrings** for all public functions and classes
- Keep functions **focused and small** (< 50 lines preferred)

### Naming Conventions

- **Modules**: lowercase_with_underscores
- **Classes**: PascalCase
- **Functions/Variables**: lowercase_with_underscores
- **Constants**: UPPER_CASE

### Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(router): add weighted random routing strategy
fix(cache): fix Redis connection timeout handling
docs(readme): update quick start guide
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/adam_gateway --cov-report=html

# Run specific test file
pytest tests/test_adapter.py

# Run tests matching a pattern
pytest -k "test_routing"
```

## Documentation

- Documentation is written in **Markdown**
- API documentation uses **OpenAPI/Swagger** format
- Keep documentation **up-to-date** with code changes

## Release Process

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a git tag: `git tag -a v0.x.x -m "Release v0.x.x"`
4. Push tag: `git push origin v0.x.x`
5. GitHub Actions will handle the release

## Questions?

Feel free to open an issue for any questions about contributing.
