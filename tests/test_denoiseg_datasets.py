import pytest
from data_portfolio import Portfolio


def test_dsb2018_n0(tmp_path):
    """Test that the DSB2018_n0 dataset downloads properly."""
    Portfolio().denoiseg.DSB2018_n0.download(tmp_path, check_md5=True)


@pytest.mark.large_dataset
def test_dsb2018_n10(tmp_path):
    """Test that the DSB2018_n10 dataset downloads properly."""
    Portfolio().denoiseg.DSB2018_n10.download(tmp_path, check_md5=True)


@pytest.mark.large_dataset
def test_dsb2018_n20(tmp_path):
    """Test that the DSB2018_n20 dataset downloads properly."""
    Portfolio().denoiseg.DSB2018_n20.download(tmp_path, check_md5=True)


def test_flywing_n0(tmp_path):
    """Test that the Flywing_n0 dataset downloads properly."""
    Portfolio().denoiseg.Flywing_n0.download(tmp_path, check_md5=True)


@pytest.mark.large_dataset
def test_flywing_n10(tmp_path):
    """Test that the Flywing_n10 dataset downloads properly."""
    Portfolio().denoiseg.Flywing_n10.download(tmp_path, check_md5=True)


@pytest.mark.large_dataset
def test_flywing_n20(tmp_path):
    """Test that the Flywing_n20 dataset downloads properly."""
    Portfolio().denoiseg.Flywing_n20.download(tmp_path, check_md5=True)


def test_mousenuclei_n0(tmp_path):
    """Test that the MouseNuclei_n0 dataset downloads properly."""
    Portfolio().denoiseg.MouseNuclei_n0.download(tmp_path, check_md5=True)


@pytest.mark.large_dataset
def test_mousenuclei_n10(tmp_path):
    """Test that the MouseNuclei_n10 dataset downloads properly."""
    Portfolio().denoiseg.MouseNuclei_n10.download(tmp_path, check_md5=True)


@pytest.mark.large_dataset
def test_mousenuclei_n20(tmp_path):
    """Test that the MouseNuclei_n20 dataset downloads properly."""
    Portfolio().denoiseg.MouseNuclei_n20.download(tmp_path, check_md5=True)


def test_unique_hashes(portfolio: Portfolio):
    """Test that all DenoiSeg dataset hashes are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    hashes = []
    for entry in portfolio.denoiseg:
        assert entry.md5_hash is not None, f"{entry.name} has no md5 hash."

        # add to list of hashes
        hashes.append(entry.md5_hash)

    assert len(hashes) == len(set(hashes)), "DenoiSeg hashes are not unique."


def test_unique_urls(portfolio: Portfolio):
    """Test that all DenoiSeg dataset URLs are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    urls = []
    for entry in portfolio.denoiseg:
        assert entry.url is not None, f"{entry.name} has no URL."

        # add to list of hashes
        urls.append(entry.url)

    assert len(urls) == len(set(urls)), "DenoiSeg URLs are not unique."
