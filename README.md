# Welcome to pymole

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPy Support](https://img.shields.io/badge/PyPy-supported-brightgreen.svg)](https://pypy.org)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/carlosal1015/pymole/ci.yml?branch=main)](https://github.com/carlosal1015/pymole/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/pymole/badge/)](https://pymole.readthedocs.io/)
[![codecov](https://codecov.io/gh/carlosal1015/pymole/branch/main/graph/badge.svg)](https://codecov.io/gh/carlosal1015/pymole)

## Overview

### Purpose and Scope

The **pymole** project is a Python library for implementing mimetic operators - discrete mathematical operators that preserve important geometric and physical properties when discretizing continuous differential operators. The library focuses on providing computationally efficient implementations of divergence, gradient, Laplacian, and interpolation operators for 1D, 2D, and 3D grids, with support for both uniform and non-uniform grid spacing.

### Project Architecture

The **pymole** library follows a hierarchical mathematical architecture where fundamental 1D operators serve as building blocks for higher-dimensional implementations. The project emphasizes scientific computing best practices with comprehensive testing, modern Python packaging, and automated quality assurance.

[Full project documentation available on DeepWiki](https://deepwiki.com/carlosal1015/pymole)

## Installation

The Python package `pymole` can be installed from GitHub:

```console
uv init
uv venv
source .venv/bin/activate
uv pip install git+https://github.com/carlosal1015/pymole.git#egg=pymole
```

## Development installation

If you want to contribute to the development of `pymole`, we recommend
the following editable installation from this repository:

```console
git clone https://github.com/carlosal1015/pymole
cd pymole
python -m pip install --editable .[tests]
```

Having done so, the test suite can be run using `pytest`:

```console
uv sync --extra=tests
uv run python -m pytest
```

```console
uv sync --extra=docs
uv run sphinx-build doc build
```

## PyPy Support

pymole fully supports PyPy for enhanced performance. To use with PyPy:

```console
pypy -m pip install git+https://github.com/carlosal1015/pymole.git#egg=pymole
```

## Project lineage

This project continues development from the original [pymole](https://github.com/nutrik/pymole)
repository (May 2018 - October 2018) with:

- 🚀 Modern Python 3.11+ support
- ✅ Comprehensive test suite (>90% coverage)
- 📚 Sphinx documentation
- 📦 Improved packaging and CI/CD
- 🧩 Expanded mimetic operator implementations
- ⚡ PyPy compatibility for performance-critical applications

## Core Features

- 1D, 2D, and 3D mimetic operators
- Uniform and non-uniform grid support
- Divergence, gradient, and Laplacian operators
- Boundary condition handling
- Mathematical property preservation
- Optimized for scientific computing

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).