import pytest

from careamics_portfolio import PortfolioManager
from careamics_portfolio.utils.pale_blue_dot import PaleBlueDot


@pytest.fixture
def pale_blue_dot() -> PaleBlueDot:
    """Fixture for the PaleBlueDot.

    Returns
    -------
    PaleBlueDot
        The PaleBlueDot picture.
    """
    return PaleBlueDot()


@pytest.fixture
def portfolio() -> PortfolioManager:
    """Fixture for the Portfolio.

    Returns
    -------
    Portfolio
        The Portfolio.
    """
    return PortfolioManager()
