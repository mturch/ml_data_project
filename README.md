# ML Data Analysis Project

A Python project for data analysis and machine learning tasks.

## Setup

1. Install dependencies with uv:
```bash
uv sync
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Start Jupyter:
```bash
jupyter notebook
```

### Alternative: Run commands directly with uv
```bash
uv run jupyter notebook
```

## Project Structure

```
ml_data_project/
├── data/                    # Raw and processed data
├── notebooks/               # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   └── 02_sql_data_analysis.ipynb
├── sql/                     # SQL queries
│   └── example_query.sql
├── src/                     # Source code modules
│   ├── data_utils.py       # Data processing utilities
│   └── sql_utils.py        # SQL database utilities
├── tests/                   # Unit tests
├── .sqlfluff               # SQLFluff configuration
├── pyproject.toml          # Project configuration
├── requirements.txt        # Legacy requirements
└── README.md
```

## SQL Development

The project includes SQLFluff for SQL linting and formatting:

```bash
# Lint SQL files
uv run sqlfluff lint sql/

# Format SQL files
uv run sqlfluff format sql/
```