import hashlib

import pytest
from data_portfolio.portfolio_entry import PortfolioEntry


class FaultyMD5(PortfolioEntry):
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
        )


# TODO change scope?
@pytest.fixture(scope="session")
def faulty_portfolio_entry():
    return FaultyMD5()
