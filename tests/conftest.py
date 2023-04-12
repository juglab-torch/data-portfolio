import hashlib

import pytest
from data_portfolio import Portfolio
from data_portfolio.portfolio_entry import PortfolioEntry


class FaultyMD5(PortfolioEntry):
    """Faulty PortfolioEntry.

    A PortfolioEntry with a faulty md5 hash.

    Attributes
    ----------
    name (str): Name of the dataset.
    url (str): URL to the dataset.
    file_name (str): Name of the file.
    md5_hash (str): Faulty MD5 hash.
    description (str): Description of the dataset.
    citation (str): Citation of the dataset.
    license (str): License of the dataset.
    files (dict): Dictionary of files.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Wikipedia logo",
            url="https://en.wikipedia.org/wiki/Wikipedia_logo#/media/File:Wikipedia-logo-v2.svg",
            file_name="Wikipedia-logo-v2.svg",
            md5_hash=hashlib.md5(b"I would prefer not to").hexdigest(),
            description="Wikipedia logo",
            citation="Wikipedia",
            license="CC BY-SA 3.0",
            files={
                ".": ["Wikipedia-logo-v2.svg"],
            },
            size=0.1,
        )


@pytest.fixture
def faulty_portfolio_entry() -> FaultyMD5:
    """Fixture for a faulty PortfolioEntry.

    Returns
    -------
    FaultyMD5
        A PortfolioEntry with a faulty md5 hash."""
    return FaultyMD5()


@pytest.fixture
def portfolio() -> Portfolio:
    """Fixture for the Portfolio.

    Returns
    -------
    Portfolio
        The Portfolio.
    """
    return Portfolio()
