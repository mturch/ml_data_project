.PHONY: help check format reqs install test clean lint sql-lint sql-format

# Default target
help:
	@echo "Available targets:"
	@echo "  help       - Show this help message"
	@echo "  install    - Install dependencies with uv"
	@echo "  check      - Run all checks (lint, type check, test)"
	@echo "  format     - Format code with black and SQL with sqlfluff"
	@echo "  lint       - Run linting (flake8, mypy)"
	@echo "  sql-lint   - Lint SQL files with sqlfluff"
	@echo "  sql-format - Format SQL files with sqlfluff"
	@echo "  test       - Run tests with pytest"
	@echo "  reqs       - Update requirements.txt from pyproject.toml"
	@echo "  clean      - Clean up temporary files"

# Install dependencies
install:
	uv sync

# Run all checks
check: lint sql-lint test
	@echo "All checks passed!"

# Format code
format:
	uv run black src/ tests/
	uv run black notebooks/ --ipynb
	@make sql-format

# Linting
lint:
	uv run flake8 src/ tests/
	uv run mypy src/

# SQL linting
sql-lint:
	uv run sqlfluff lint sql/

# SQL formatting  
sql-format:
	uv run sqlfluff format sql/

# Run tests
test:
	uv run pytest tests/ -v

# Update requirements.txt from pyproject.toml
reqs:
	uv pip compile pyproject.toml -o requirements.txt

# Clean temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

# Development setup
dev-setup: install
	uv run pre-commit install