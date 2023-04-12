import pytest
from data_portfolio import Portfolio

# TODO check that the downloaded files are correct


@pytest.mark.dataset
@pytest.mark.large_dataset
def test_n2v_bsd68(tmp_path):
    """Test that the N2V_BSD68 dataset downloads properly."""
    Portfolio().denoising.N2V_BSD68.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_n2v_sem(tmp_path):
    """Test that the N2V_SEM dataset downloads properly."""
    Portfolio().denoising.N2V_SEM.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_n2v_rgb(tmp_path):
    """Test that the N2V_RGB dataset downloads properly."""
    Portfolio().denoising.N2V_RGB.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_flywing(tmp_path):
    """Test that the flywing dataset downloads properly."""
    Portfolio().denoising.flywing.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_unique_hashes(portfolio: Portfolio):
    """Test that all Denoising dataset hashes are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    hashes = []
    for entry in portfolio.denoising:
        assert entry.md5_hash is not None, f"{entry.name} has no md5 hash."

        # add to list of hashes
        hashes.append(entry.md5_hash)

    assert len(hashes) == len(set(hashes)), "Denoising hashes are not unique."


def test_unique_urls(portfolio: Portfolio):
    """Test that all Denoising dataset URLs are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    urls = []
    for entry in portfolio.denoising:
        assert entry.url is not None, f"{entry.name} has no URL."

        # add to list of hashes
        urls.append(entry.url)

    assert len(urls) == len(set(urls)), "Denoising URLs are not unique."
