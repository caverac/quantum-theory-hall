# Quantum Theory for Mathematicians (Hall) Solutions

[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue.svg)](https://caverac.github.io/quantum-theory-hall/)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p align="center">
  <a href="https://caverac.github.io/quantum-theory-hall/">
    <img src="https://img.shields.io/badge/📖_View_Solutions-Online-4a5568?style=for-the-badge" alt="View Solutions Online">
  </a>
</p>

Solutions to the problem sets from Brian C. Hall's *Quantum Theory for Mathematicians*. This repository contains Python implementations of numerical solutions, leveraging libraries such as NumPy, SciPy, and Matplotlib for efficient computation and visualization.

## About

This project provides detailed solutions to problems from the textbook *Quantum Theory for Mathematicians* by Brian C. Hall (Graduate Texts in Mathematics, Vol. 267, Springer, 2013). The solutions are implemented in Python and organized by chapter, featuring:

- **Analytical derivations** with step-by-step mathematical explanations
- **Numerical implementations** using modern Python scientific computing stack
- **Visualizations** with publication-quality plots
- **Interactive documentation** with mathematical formulas and figures

## Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/caverac/quantum-theory-hall.git
   cd quantum-theory-hall
   ```

1. Install dependencies using uv:

   ```bash
   uv sync
   ```

   Or using pip:

   ```bash
   pip install -e .
   ```

### Running the Code

Generate figures and run solutions:

```bash
# Generate plots
uv run python scripts/generate_assets.py

# Run all tests
uv run pytest

# Build documentation
uv run mkdocs serve

# Build documentation - live
uv run mkdocs serve --livereload
```

## Documentation

The complete documentation with mathematical derivations, figures, and code explanations is available at:

**[https://caverac.github.io/quantum-theory-hall/](https://caverac.github.io/quantum-theory-hall/)**

### Local Documentation

To build and serve the documentation locally:

```bash
uv run mkdocs serve
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

## Project Structure

```
quantum-theory-hall/
├── docs/                          # Documentation source
│   ├── assets/                    # Generated figures and images
│   ├── chapterX.md                # Chapter X solutions
│   └── index.md                   # Homepage
├── quantum_theory_hall/        # Source code
│   └── chapterX/                  # Chapter X implementations
│       └── y.py                   # Implementation for problem y
├── tests/                         # Test suite
│   └── unit/                      # Unit tests
├── scripts/                       # Utility scripts
├── main.py                        # MkDocs macro definitions
├── pyproject.toml                 # Project configuration
└── mkdocs.yml                     # Documentation configuration
```

## Development

### Setting up Development Environment

1. Install development dependencies:

   ```bash
   uv sync --group dev
   ```

1. Install pre-commit hooks:

   ```bash
   uv run pre-commit install
   ```

1. Run code quality checks:

   ```bash
   # Format code
   uv run black quantum_theory_hall tests

   # Lint code
   uv run flake8 quantum_theory_hall

   # Type checking
   uv run mypy quantum_theory_hall

   # Run tests
   uv run pytest
   ```

### Generating Releases

This project uses [Commitizen](https://commitizen-tools.github.io/commitizen/) for semantic versioning:

```bash
# Bump version and create changelog
uv run cz bump

# Push changes and tags
git push --follow-tags
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:

- Setting up the development environment
- Code style and quality standards
- Submitting pull requests
- Adding new problem solutions

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

**Carlos Vera-Ciro** - [caverac@gmail.com](mailto:caverac@gmail.com)

Project Link: [https://github.com/caverac/quantum-theory-hall](https://github.com/caverac/quantum-theory-hall)

## References

Hall, B. C. (2013). *Quantum Theory for Mathematicians*. Graduate Texts in Mathematics, Vol. 267. Springer.
