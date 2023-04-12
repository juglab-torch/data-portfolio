import pytest
from data_portfolio import Portfolio
from data_portfolio.portfolio_entry import PortfolioEntry

from .utils import (
    download_checker,
    list_heavy_datasets,
    list_light_datasets,
    portoflio_entry_checker,
    unique_md5_checker,
    unique_url_checker,
)

LIGHT_DATASETS = list_light_datasets(Portfolio().denoising)
HEAVY_DATASETS = list_heavy_datasets(Portfolio().denoising)


@pytest.mark.parametrize("dataset", LIGHT_DATASETS)
def test_light_datasets(tmp_path, dataset: PortfolioEntry):
    """Test that all light denoising datasets download properly.

    This test also checks the files and size.

    Parameters
    ----------
    tmp_path : Path
        Path to temporary directory.
    dataset : Dataset
        Dataset object.
    """
    download_checker(tmp_path, dataset)


@pytest.mark.large_dataset
@pytest.mark.parametrize("dataset", HEAVY_DATASETS)
def test_heavy_datasets(tmp_path, dataset):
    """Test that all heavy denoising datasets download properly.

    This test also checks the files and size.

    Parameters
    ----------
    tmp_path : Path
        Path to temporary directory.
    dataset : Dataset
        Dataset object.
    """
    download_checker(tmp_path, dataset)


def test_unique_hashes(portfolio: Portfolio):
    """Test that all denoising dataset hashes are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    unique_md5_checker(portfolio.denoising)


def test_unique_urls(portfolio: Portfolio):
    """Test that all denoising dataset URLs are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    unique_url_checker(portfolio.denoising)


def test_no_empty_dataset_entry(portfolio: Portfolio):
    """Test that no denoising dataset entry is empty.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    for entry in portfolio.denoising:
        portoflio_entry_checker(entry)
