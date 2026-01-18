# Contributing to Quantum Mechanics Solutions

Thank you for your interest in contributing to this project! This guide will help you get started with contributing solutions, improvements, and documentation to the Quantum Theory for Mathematicians problem set solutions.

## Ways to Contribute

- **Add new problem solutions** from Hall's textbook
- **Improve existing solutions** with better algorithms or explanations
- **Fix bugs** in calculations or code
- **Enhance documentation** with clearer explanations
- **Add visualizations** and interactive plots
- **Improve code quality** and performance
- **Write tests** for numerical solutions

## Getting Started

### 1. Set Up Development Environment

1. **Fork the repository** on GitHub

1. **Clone your fork** locally:

   ```bash
   git clone https://github.com/your-username/quantum-theory-hall.git
   cd quantum-theory-hall
   ```

1. **Install uv** (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

1. **Set up the development environment**:

   ```bash
   uv sync --all-groups
   ```

1. **Install pre-commit hooks**:

   ```bash
   uv run pre-commit install
   ```

### 2. Create a Feature Branch

```bash
git checkout -b feature/chapter-X-problem-Y
# or
git checkout -b fix/issue-description
# or
git checkout -b docs/improve-explanation
```

## Contributing Guidelines

### Code Style and Quality

We maintain high code quality standards:

#### Python Code Style

- **Formatter**: [Black](https://black.readthedocs.io/) (line length: 120)
- **Linter**: [Flake8](https://flake8.pycqa.org/)
- **Type Checker**: [MyPy](https://mypy.readthedocs.io/)

Run quality checks:

```bash
# Format code
uv run black quantum_theory_hall tests

# Check formatting
uv run black --check quantum_theory_hall tests

# Lint code
uv run flake8 quantum_theory_hall

# Type checking
uv run mypy quantum_theory_hall

```

#### Documentation Style

- **Markdown**: Use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) syntax
- **Math**: Use LaTeX syntax with custom macros
- **Figures**: Save as PNG in `docs/assets/` with descriptive names

### Adding New Problem Solutions

#### 1. Code Structure

Create new solutions following this structure:

```python
"""Problem X.Y: Brief description.

Detailed explanation of the physical problem and approach.
"""

import logging
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

logger = logging.getLogger(__name__)


def solve_problem_xy() -> tuple[np.ndarray, np.ndarray]:
    """Solve Problem X.Y analytically/numerically.

    Returns
    -------
    tuple
        (x_values, y_values) for plotting
    """
    # Implementation here
    return x_values, y_values


def plot_problem_xy() -> None:
    """Generate publication-quality plot for Problem X.Y."""
    # Configure matplotlib for Times New Roman font
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman', 'Times']
    plt.rcParams['mathtext.fontset'] = 'stix'

    fig, ax = plt.subplots(figsize=(6.5, 5))

    # Your plotting code here

    # Save figure
    fig.savefig(
        f"docs/assets/chapter{X}_problem{Y}.png",
        dpi=300,
        bbox_inches='tight',
        facecolor='white',
        edgecolor='none'
    )


if __name__ == "__main__":
    plot_problem_xy()
```

#### 2. Tests

Write unit tests for your solution:

```python
"""Tests for Problem X.Y solution."""

import pytest
import numpy as np
from quantum_theory_hall.chapter0X.problem_xy import solve_problem_xy


class TestProblemXY:
    """Test cases for Problem X.Y."""

    def test_solution_properties(self):
        """Test that solution has expected properties."""
        x, y = solve_problem_xy()

        # Test array properties
        assert len(x) == len(y)
        assert np.all(np.isfinite(x))
        assert np.all(np.isfinite(y))

    def test_physical_constraints(self):
        """Test that solution satisfies physical constraints."""
        # Add specific physics tests
        pass
```

### Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

feat(chapter1): add solution for Problem 1.5
fix(harmonic): correct sign error in energy equation
docs(readme): update installation instructions
test(chapter1): add tests for Problem 1.1
```

**Types:**

- `feat`: New feature or solution
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Maintenance tasks

## Testing

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=quantum_theory_hall

# Run specific test file
uv run pytest tests/unit/quantum_theory_hall/chapter01/test_example.py

# Run with verbose output
uv run pytest -v
```

## Pull Request Process

### Before Submitting

1. **Update your branch**:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

1. **Run all quality checks**:

   ```bash
   uv run black quantum_theory_hall tests
   uv run flake8 quantum_theory_hall
   uv run mypy quantum_theory_hall
   uv run pytest
   ```

1. **Update documentation**:

   ```bash
   uv run mkdocs build --strict
   ```

1. **Commit your changes**:

   ```bash
   git add .
   git commit -m "feat(chapter1): add solution for Problem 1.5"
   ```

### Submitting the PR

1. **Push to your fork**:

   ```bash
   git push origin feature/chapter-X-problem-Y
   ```

1. **Create Pull Request** on GitHub with:

   - Clear title following conventional commits
   - Detailed description of changes
   - Reference to related issues
   - Screenshots/plots if applicable

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to advancing quantum mechanics education!
