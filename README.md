# Data Portfolio

[![License](https://img.shields.io/pypi/l/data-portfolio.svg?color=green)](https://github.com/juglab-torch/data-portfolio/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/data-portfolio.svg?color=green)](https://pypi.org/project/data-portfolio)
[![Python Version](https://img.shields.io/pypi/pyversions/data-portfolio.svg?color=green)](https://python.org)
[![CI](https://github.com/juglab-torch/data-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/juglab-torch/data-portfolio/actions/workflows/ci.yml)
[![Datasets CI](https://github.com/juglab-torch/data-portfolio/actions/workflows/datasets_ci.yml/badge.svg)](https://github.com/juglab-torch/data-portfolio/actions/workflows/datasets_ci.yml)
[![codecov](https://codecov.io/gh/juglab-torch/data-portfolio/branch/main/graph/badge.svg)](https://codecov.io/gh/juglab-torch/data-portfolio)

A helper package to download example datasets used in various publications by the Jug lab, including data featured in N2V, P(P)N2V, DivNoising, HDN, EmbedSeg, etc.

The complete list of datasets can be found [here](datasets/datasets.json).

## Installation

To install the portfolio in your conda environment, simply use `pip`:
```bash
$ pip install data-portfolio
```

## Usage

Follow the [example notebook](examples/example.ipynb) for details on how to use the package.

The portfolio can be instantiated as follow:

```python
from data_portfolio import Portfolio

portfolio = Portfolio()
```

You can explore the different datasets easily:
```python
print(portfolio)
print(portfolio.denoising)
print(portfolio.denoising.N2V_SEM)
```

Finally, you can download the dataset of your choice:
```python
from pathlib import Path

data_path = Path('data')
portfolio.denoising.N2V_SEM.download(data_path)
```
