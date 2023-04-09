import pytest
import hashlib


def test_faulty_md5(tmp_path, faulty_portfolio_entry):
    """Test that faulty md5 hash raises an error."""

    # test that it downloads fine when not checking md5 hash
    faulty_portfolio_entry.download(tmp_path, check_md5=False)
    assert (tmp_path / faulty_portfolio_entry.file_name).exists()

    with pytest.raises(ValueError):
        faulty_portfolio_entry.download(tmp_path, check_md5=True)


def test_change_entry(faulty_portfolio_entry):
    faulty_portfolio_entry.md5_hash = hashlib.md5(b"Malicious file hash").hexdigest()
