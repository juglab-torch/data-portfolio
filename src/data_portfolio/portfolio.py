from dataclasses import dataclass

from .denoising_datasets import N2V_BSD68, N2V_SEM, N2V_RGB, Flywing
from .denoiseg_datasets import NoiseLevel, DSB2018, SegFlywing, MouseNuclei


class DenoiSeg:
    """Ensemble of DenoiSeg datasets.
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
        return self._DSB2018_n0
    
    @property
    def DSB2018_n10(self) -> DSB2018:
        return self._DSB2018_n10
    
    @property
    def DSB2018_n20(self) -> DSB2018:
        return self._DSB2018_n20
    
    @property
    def Flywing_n0(self) -> SegFlywing:
        return self._SegFlywing_n0
    
    @property
    def Flywing_n10(self) -> SegFlywing:
        return self._SegFlywing_n10
    
    @property
    def Flywing_n20(self) -> SegFlywing:
        return self._SegFlywing_n20
    
    @property
    def MouseNuclei_n0(self) -> MouseNuclei:
        return self._MouseNuclei_n0
    
    @property
    def MouseNuclei_n10(self) -> MouseNuclei:
        return self._MouseNuclei_n10
    
    @property
    def MouseNuclei_n20(self) -> MouseNuclei:
        return self._MouseNuclei_n20

    # TODO build from attributes rather than manually
    @staticmethod
    def list_datasets() -> list[str]:
        return ["DSB2018_n0", "DSB2018_n10", "DSB2018_n20",
                "Flywing_n0", "Flywing_n10", "Flywing_n20",
                "MouseNuclei_n0", "MouseNuclei_n10", "MouseNuclei_n20"]

    def __str__(self) -> str:
        return f"Segmentation datasets: {self.list_datasets()}"
    

class Denoising:
    """ Ensemble of denoising datasets.
    """

    def __init__(self) -> None:
        self._N2V_BSD68 = N2V_BSD68()
        self._N2V_SEM = N2V_SEM()
        self._N2V_RGB = N2V_RGB()
        self._flywing = Flywing()

    @property
    def N2V_BSD68(self) -> N2V_BSD68:
        return self._N2V_BSD68

    @property
    def N2V_SEM(self) -> None:
        return self._N2V_SEM

    @property
    def N2V_RGB(self) -> None:
        return self._N2V_RGB

    @property
    def flywing(self) -> None:
        return self._flywing

    @staticmethod
    def list_datasets() -> list[str]:
        return ["N2V_BSD", "N2V_SEM", "N2V_RGB", "flywing"]

    def __str__(self) -> str:
        return f"Denoising datasets: {self.list_datasets()}"

@dataclass
class Portfolio:

    def __init__(self) -> None:
        self._denoising = Denoising()
        self._denoiseg = DenoiSeg()

    @property
    def denoising(self) -> Denoising:
        return self._denoising
    
    @property
    def denoiseg(self) -> DenoiSeg:
        return self._denoiseg

    def __str__(self) -> str:
        return f"Portfolio:\nDenoising datasets: {self.denoising.list_datasets()}\nDenoiSeg datasets: {self.denoiseg.list_datasets()}"
        f""
