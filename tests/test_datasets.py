import pytest

from data_portfolio import Portfolio


def test_faulty_md5(tmp_path, faulty_portfolio_entry):
    """Test that faulty md5 hash raises an error."""

    # test that it downloads fine when not checking md5 hash
    faulty_portfolio_entry.download(tmp_path, check_md5=False)
    assert (tmp_path / faulty_portfolio_entry.file_name).exists()

    with pytest.raises(ValueError):
        faulty_portfolio_entry.download(tmp_path, check_md5=True)

@pytest.mark.dataset
def test_n2v_bsd68(tmp_path):
    """Test that N2V_BSD68 dataset downloads properly."""
    Portfolio().denoising.N2V_BSD68.download(tmp_path, check_md5=True)


@pytest.mark.dataset
def test_n2v_sem(tmp_path):
    """Test that N2V_SEM dataset downloads properly."""
    Portfolio().denoising.N2V_SEM.download(tmp_path, check_md5=True)