import json
from dataclasses import dataclass
from json import JSONEncoder
from pathlib import Path
from typing import Dict, List, Union

from .denoiseg_datasets import DSB2018, MouseNuclei, NoiseLevel, SegFlywing
from .denoising_datasets import N2V_BSD68, N2V_RGB, N2V_SEM, Flywing
from .portfolio_entry import PortfolioEntry


# TODO make portfolios iterable
class IterablePortfolio:
    """Iterable portfolio class."""

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """Name of the portfolio.

        Returns
        -------
        str
            Name of the portfolio.
        """
        return self._name

    def list_datasets(self) -> List[str]:
        """List of datasets in the portfolio.

        Returns
        -------
        list[str]
            List of datasets in the portfolio.
        """
        attributes = []

        # for each attribute
        for attribute in vars(self).values():
            if isinstance(attribute, PortfolioEntry):
                attributes.append(attribute.name)

        return attributes

    def as_dict(self) -> Dict[str, Dict[str, str]]:
        """Dictionary representation of a portfolio.

        Returns
        -------
        dict[str]
            Dictionary representation of the DenoiSeg portfolio.
        """
        entries = {}

        # for each attribute
        for attribute in vars(self).values():
            # if the attribute is a PortfolioEntry
            if isinstance(attribute, PortfolioEntry):
                # add the attribute to the entries dictionary
                entries[attribute.name] = {
                    "URL": attribute.url,
                    "Citation": attribute.citation,
                }
        return entries

    def __str__(self) -> str:
        """String representation of a portfolio.

        Returns
        -------
        str
        String representation of a portfolio.
        """
        return f"Denoising datasets: {self.list_datasets()}"


class PortfolioEncoder(JSONEncoder):
    """Portfolio encoder class."""

    def default(self, o: IterablePortfolio) -> Dict[str, Dict[str, str]]:
        """Default method for json export.

        Parameters
        ----------
        o : IterablePortfolio
            Portfolio to export.

        Returns
        -------
        dict[str, str]
            Dictionary representation of the portfolio.
        """
        return o.as_dict()


class DenoiSeg(IterablePortfolio):
    """Portfolio of DenoiSeg datasets.

    Attributes
    ----------
        DSB2018_n0 (DSB2018): DSB2018 dataset with noise level 0.
        DSB2018_n10 (DSB2018): DSB2018 dataset with noise level 10.
        DSB2018_n20 (DSB2018): DSB2018 dataset with noise level 20.
        Flywing_n0 (SegFlywing): Flywing dataset with noise level 0.
        Flywing_n10 (SegFlywing): Flywing dataset with noise level 10.
        Flywing_n20 (SegFlywing): Flywing dataset with noise level 20.
        MouseNuclei_n0 (MouseNuclei): MouseNuclei dataset with noise level 0.
        MouseNuclei_n10 (MouseNuclei): MouseNuclei dataset with noise level 10.
        MouseNuclei_n20 (MouseNuclei): MouseNuclei dataset with noise level 20.
    """

    def __init__(self) -> None:
        super().__init__("DenoiSeg")

        self._DSB2018_n0 = DSB2018(NoiseLevel.N0)
        self._DSB2018_n10 = DSB2018(NoiseLevel.N10)
        self._DSB2018_n20 = DSB2018(NoiseLevel.N20)
        self._SegFlywing_n0 = SegFlywing(NoiseLevel.N0)
        self._SegFlywing_n10 = SegFlywing(NoiseLevel.N10)
        self._SegFlywing_n20 = SegFlywing(NoiseLevel.N20)
        self._MouseNuclei_n0 = MouseNuclei(NoiseLevel.N0)
        self._MouseNuclei_n10 = MouseNuclei(NoiseLevel.N10)
        self._MouseNuclei_n20 = MouseNuclei(NoiseLevel.N20)

    @property
    def DSB2018_n0(self) -> DSB2018:
        """DSB2018 dataset with noise level 0.

        Returns
        -------
        DSB2018
            DSB2018 dataset with noise level 0.
        """
        return self._DSB2018_n0

    @property
    def DSB2018_n10(self) -> DSB2018:
        """DSB2018 dataset with noise level 10.

        Returns
        -------
        DSB2018
            DSB2018 dataset with noise level 10.
        """
        return self._DSB2018_n10

    @property
    def DSB2018_n20(self) -> DSB2018:
        """DSB2018 dataset with noise level 20.

        Returns
        -------
        DSB2018
            DSB2018 dataset with noise level 20.
        """
        return self._DSB2018_n20

    @property
    def Flywing_n0(self) -> SegFlywing:
        """Flywing dataset with noise level 0.

        Returns
        -------
        SegFlywing
            Flywing dataset with noise level 0.
        """
        return self._SegFlywing_n0

    @property
    def Flywing_n10(self) -> SegFlywing:
        """Flywing dataset with noise level 10.

        Returns
        -------
        SegFlywing
            Flywing dataset with noise level 10.
        """
        return self._SegFlywing_n10

    @property
    def Flywing_n20(self) -> SegFlywing:
        """Flywing dataset with noise level 20.

        Returns
        -------
        SegFlywing
            Flywing dataset with noise level 20.
        """
        return self._SegFlywing_n20

    @property
    def MouseNuclei_n0(self) -> MouseNuclei:
        """MouseNuclei dataset with noise level 0.

        Returns
        -------
        MouseNuclei
            MouseNuclei dataset with noise level 0.
        """
        return self._MouseNuclei_n0

    @property
    def MouseNuclei_n10(self) -> MouseNuclei:
        """MouseNuclei dataset with noise level 10.

        Returns
        -------
        MouseNuclei
            MouseNuclei dataset with noise level 10.
        """
        return self._MouseNuclei_n10

    @property
    def MouseNuclei_n20(self) -> MouseNuclei:
        """MouseNuclei dataset with noise level 20.

        Returns
        -------
        MouseNuclei
            MouseNuclei dataset with noise level 20.
        """
        return self._MouseNuclei_n20


class Denoising(IterablePortfolio):
    """Ensemble of denoising datasets.

    Attributes
    ----------
    N2V_BSD68 (N2V_BSD68): BSD68 dataset.
    N2V_SEM (N2V_SEM): SEM dataset.
    N2V_RGB (N2V_RGB): RGB dataset.
    flywing (Flywing): Flywing dataset.
    """

    def __init__(self) -> None:
        super().__init__("Denoising")

        self._N2V_BSD68 = N2V_BSD68()
        self._N2V_SEM = N2V_SEM()
        self._N2V_RGB = N2V_RGB()
        self._flywing = Flywing()

    @property
    def N2V_BSD68(self) -> N2V_BSD68:
        """BSD68 dataset.

        Returns
        -------
        N2V_BSD68
            BSD68 dataset.
        """
        return self._N2V_BSD68

    @property
    def N2V_SEM(self) -> N2V_SEM:
        """SEM dataset.

        Returns
        -------
        N2V_SEM
            SEM dataset.
        """
        return self._N2V_SEM

    @property
    def N2V_RGB(self) -> N2V_RGB:
        """RGB dataset.

        Returns
        -------
        N2V_RGB
            RGB dataset.
        """
        return self._N2V_RGB

    @property
    def flywing(self) -> Flywing:
        """Flywing dataset.

        Returns
        -------
        Flywing
        Flywing dataset.
        """
        return self._flywing


@dataclass
class Portfolio:
    """Portfolio of datasets.

    Attributes
    ----------
    denoising (Denoising): Denoising datasets.
    denoiseg (DenoiSeg): DenoiSeg datasets.
    """

    def __init__(self) -> None:
        self._denoising = Denoising()
        self._denoiseg = DenoiSeg()

    @property
    def denoising(self) -> Denoising:
        """Denoising datasets.

        Returns
        -------
        Denoising
        Denoising datasets.
        """
        return self._denoising

    @property
    def denoiseg(self) -> DenoiSeg:
        """DenoiSeg datasets.

        Returns
        -------
        DenoiSeg
        DenoiSeg datasets.
        """
        return self._denoiseg

    def __str__(self) -> str:
        """String representation of the portfolio.

        This method allows having a frendly representation of the portfolio as string.

        Returns
        -------
        str
        String representation of the portfolio.
        """
        return (
            f"Portfolio:\n"
            f"Denoising datasets: {self.denoising.list_datasets()}\n"
            f"DenoiSeg datasets: {self.denoiseg.list_datasets()}"
        )

    def as_dict(self) -> dict[str, IterablePortfolio]:
        """Portfolio as dictionary.

        This method is used during json serialization to maintain human readable
        keys.

        Returns
        -------
        dict[str, IterablePortfolio]
            Portfolio as dictionary.
        """
        attributes = {}

        for attribute in vars(self).values():
            attributes[attribute.name] = attribute

        return attributes

    def to_json(self, path: Union[str, Path]) -> None:
        """Save portfolio to json file using the `as_dict` method.

        Parameters
        ----------
        path : str or Path
            Path to json file.
        """
        with open(path, "w") as f:
            json.dump(self.as_dict(), f, indent=4, cls=PortfolioEncoder)
