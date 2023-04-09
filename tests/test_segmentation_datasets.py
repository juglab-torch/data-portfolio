import pytest

from data_portfolio import Portfolio
from data_portfolio.segmentation_datasets import NoiseLevel

@pytest.mark.dataset
def test_dsb2018_n0(tmp_path):
    """Test that the DSB2018_n0 dataset downloads properly."""
    Portfolio().segmentation.DSB2018_n0.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_dsb2018_n10(tmp_path):
    """Test that the DSB2018_n10 dataset downloads properly."""
    Portfolio().segmentation.DSB2018_n10.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_dsb2018_n20(tmp_path):
    """Test that the DSB2018_n20 dataset downloads properly."""
    Portfolio().segmentation.DSB2018_n20.download(tmp_path, check_md5=True)

