# Welcome to pymole

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/carlosal1015/pymole/ci.yml?branch=main)](https://github.com/carlosal1015/pymole/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/pymole/badge/)](https://pymole.readthedocs.io/)
[![codecov](https://codecov.io/gh/carlosal1015/pymole/branch/main/graph/badge.svg)](https://codecov.io/gh/carlosal1015/pymole)

## Installation

The Python package `pymole` can be installed from PyPI:

```
python -m pip install pymole
```

## Development installation

If you want to contribute to the development of `pymole`, we recommend
the following editable installation from this repository:

```
git clone https://github.com/carlosal1015/pymole
cd pymole
python -m pip install --editable .[tests]
```

Having done so, the test suite can be run using `pytest`:

```
python -m pytest
```

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).
