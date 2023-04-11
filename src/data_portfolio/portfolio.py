from dataclasses import dataclass
from typing import List

from .denoiseg_datasets import DSB2018, MouseNuclei, NoiseLevel, SegFlywing
from .denoising_datasets import N2V_BSD68, N2V_RGB, N2V_SEM, Flywing


class DenoiSeg:
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

    # TODO build from attributes rather than manually
    @staticmethod
    def list_datasets() -> List[str]:
        """List datasets in the DenoiSeg ensemble.

        Returns
        -------
        list[str]
        List of datasets.
        """
        return [
            "DSB2018_n0",
            "DSB2018_n10",
            "DSB2018_n20",
            "Flywing_n0",
            "Flywing_n10",
            "Flywing_n20",
            "MouseNuclei_n0",
            "MouseNuclei_n10",
            "MouseNuclei_n20",
        ]

    def __str__(self) -> str:
        """String representation of the DenoiSeg portfolio.

        Returns
        -------
        str
            String representation of the DenoiSeg portfolio.
        """
        return f"Segmentation datasets: {self.list_datasets()}"


class Denoising:
    """Ensemble of denoising datasets.

    Attributes
    ----------
    N2V_BSD68 (N2V_BSD68): BSD68 dataset.
    N2V_SEM (N2V_SEM): SEM dataset.
    N2V_RGB (N2V_RGB): RGB dataset.
    flywing (Flywing): Flywing dataset.
    """

    def __init__(self) -> None:
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

    @staticmethod
    def list_datasets() -> List[str]:
        """List datasets in the Denoising ensemble.

        Returns
        -------
        list[str]
        List of datasets.
        """
        return ["N2V_BSD", "N2V_SEM", "N2V_RGB", "flywing"]

    def __str__(self) -> str:
        """String representation of the Denoising portfolio.

        Returns
        -------
        str
        String representation of the Denoising portfolio.
        """
        return f"Denoising datasets: {self.list_datasets()}"


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
