import pytest

from data_portfolio import Portfolio


@pytest.mark.dataset
def test_n2v_bsd68(tmp_path):
    """Test that N2V_BSD68 dataset downloads properly."""
    Portfolio().denoising.N2V_BSD68.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_n2v_sem(tmp_path):
    """Test that N2V_SEM dataset downloads properly."""
    Portfolio().denoising.N2V_SEM.download(tmp_path, check_md5=True)