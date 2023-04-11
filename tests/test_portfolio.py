from data_portfolio import Portfolio


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
