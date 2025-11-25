# Project Setup with Pre-commit and Ruff

This project uses [pre-commit](https://pre-commit.com/) hooks with [Ruff](https://docs.astral.sh/ruff/) for code linting and formatting.

## Prerequisites

- Python 3.9 or higher
- pip for package installation

## Installation

### 1. Install pre-commit

Using pip:
```bash
pip install pre-commit
```

### 2. Install Ruff

Using pip:
```bash
pip install ruff
```

### 3. Install pre-commit hooks

After cloning the repository, install the pre-commit hooks:

```bash
pre-commit install
```

## Usage

### Pre-commit Hooks

The hooks will automatically run on every commit. The configuration includes:

- **ruff**: Linting with automatic fixes
- **ruff-format**: Code formatting

### Manual Commands

#### Run pre-commit on all files:
```bash
pre-commit run --all-files
```

#### Run pre-commit on specific files:
```bash
pre-commit run --files path/to/file.py
```
#### Run pre-commit on staged files:
```bash
pre-commit run
```


#### Run only ruff linting:
```bash
ruff check . --fix
```

#### Run only ruff formatting:
```bash
ruff format .
```

#### Run ruff formatting for specific files:
```bash
ruff format path/to/file.py
```


#### Check formatting without making changes:
```bash
ruff format . --check
```

### Ruff Configuration

The project uses custom Ruff configuration defined in `pyproject.toml`:

- **Line length**: 79 characters
- **Target Python version**: 3.9
- **Indent width**: 4 spaces
- **Quote style**: Double quotes
- **Linting rules**: Pyflakes (F) and pycodestyle (E4, E7, E9)

## Bypassing Hooks

If you need to commit without running hooks (not recommended):

```bash
git commit --no-verify -m "your commit message"
```

## Troubleshooting

### Update pre-commit hooks:
```bash
pre-commit autoupdate
```

### Clean pre-commit cache:
```bash
pre-commit clean
```

### Uninstall hooks:
```bash
pre-commit uninstall
```

## Files

- `.pre-commit-config.yaml`: Pre-commit configuration
- `pyproject.toml`: Ruff configuration and project settings