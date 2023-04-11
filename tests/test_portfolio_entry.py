import pytest
from data_portfolio import Portfolio


def test_faulty_md5(tmp_path, faulty_portfolio_entry):
    """Test that faulty md5 hash raises an error.

    Parameters
    ----------
        tmp_path (Path): Path to temporary directory.
        faulty_portfolio_entry (FaultyMD5): test PortfolioEntry
    """

    # test that it downloads fine when not checking md5 hash
    faulty_portfolio_entry.download(tmp_path, check_md5=False)
    assert (tmp_path / faulty_portfolio_entry.file_name).exists()

    with pytest.raises(ValueError):
        faulty_portfolio_entry.download(tmp_path, check_md5=True)


def test_change_entry(faulty_portfolio_entry):
    """Check that changing a PortfolioEntry member raises an error.

    Parameters
    ----------
    faulty_portfolio_entry : FaultyMD5
        Test PortfolioEntry.
    """
    # Verify that we can access the members
    faulty_portfolio_entry.name
    faulty_portfolio_entry.url
    faulty_portfolio_entry.description
    faulty_portfolio_entry.license
    faulty_portfolio_entry.citation
    faulty_portfolio_entry.file_name
    faulty_portfolio_entry.md5_hash
    faulty_portfolio_entry.files

    # Check that changing members raises errors
    with pytest.raises(AttributeError):
        faulty_portfolio_entry.name = ""

    with pytest.raises(AttributeError):
        faulty_portfolio_entry.url = ""

    with pytest.raises(AttributeError):
        faulty_portfolio_entry.description = ""

    with pytest.raises(AttributeError):
        faulty_portfolio_entry.license = ""

    with pytest.raises(AttributeError):
        faulty_portfolio_entry.citation = ""

    with pytest.raises(AttributeError):
        faulty_portfolio_entry.file_name = ""

    with pytest.raises(AttributeError):
        faulty_portfolio_entry.md5_hash = ""

    with pytest.raises(AttributeError):
        faulty_portfolio_entry.files = {}


def test_portfolios_as_iterable(portfolio: Portfolio):
    """Test that portfolios are iterable.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio to test.
    """
    # denoiseg
    denoiseg_entries = [entry.name for entry in portfolio.denoiseg]
    assert denoiseg_entries == portfolio.denoiseg.list_datasets()

    # denoising
    denoising_entries = [entry.name for entry in portfolio.denoising]
    assert denoising_entries == portfolio.denoising.list_datasets()


def test_list_datasets(portfolio: Portfolio):
    """Test that the list_datasets method works on portfolios.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio to test.
    """
    # denoiseg
    denoiseg_list = portfolio.denoiseg.list_datasets()
    assert len(denoiseg_list) > 0

    for entry in denoiseg_list:
        assert entry in portfolio.denoiseg.as_dict().keys()

    # denoising
    denoising_list = portfolio.denoising.list_datasets()
    assert len(denoising_list) > 0

    for entry in denoising_list:
        assert entry in portfolio.denoising.as_dict().keys()


def test_portfolio_as_dict(portfolio: Portfolio):
    """Test that the as_dict method works on portfolios.

    Parameters:
    -----------
    portfolio : Portfolio
        Portfolio to test.
    """
    portfolio_dict = portfolio.as_dict()
    assert len(portfolio_dict) > 0
    assert portfolio.denoiseg.name in portfolio_dict
    assert portfolio.denoising.name in portfolio_dict

    # denoiseg
    denoiseg_dict = portfolio.denoiseg.as_dict()
    assert len(denoiseg_dict) > 0

    # check entries
    for entry in denoiseg_dict.values():
        assert "URL" in entry
        assert "Citation" in entry

    # denoising
    denoising_dict = portfolio.denoising.as_dict()
    assert len(denoising_dict) > 0

    # same here
    for entry in denoising_dict.values():
        assert "URL" in entry
        assert "Citation" in entry


def test_export_to_json(tmp_path, portfolio: Portfolio):
    """Test that the export Portfolio to json works.

    Parameters
    ----------
    tmp_path : Path
        Temporary path.
    portfolio : Portfolio
        Portfolio to test.
    """
    import json

    # export to json
    path_to_file = tmp_path / "portfolio.json"
    portfolio.to_json(path_to_file)

    # check that the file exists
    assert path_to_file.exists()

    # load json file
    with open(path_to_file) as f:
        data = json.load(f)

        assert portfolio.denoiseg.name in data
        assert data[portfolio.denoiseg.name] == portfolio.denoiseg.as_dict()
        assert portfolio.denoising.name in data
        assert data[portfolio.denoising.name] == portfolio.denoising.as_dict()
