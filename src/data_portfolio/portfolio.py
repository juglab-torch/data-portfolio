from dataclasses import dataclass

from .datasets import N2V_BSD68, N2V_SEM, N2V_RGB


class Segmentation:
    """Ensemble of segmentation datasets.
    """
    def __init__(self) -> None:
        self._DSB2018 = None

    @staticmethod
    def list_datasets() -> list[str]:
        return []

    def __str__(self) -> str:
        return f"Segmentation datasets: {self.list_datasets()}"
    

class Denoising:
    """ Ensemble of denoising datasets.
    """

    def __init__(self) -> None:
        self._N2V_BSD68 = N2V_BSD68()
        self._N2V_SEM = N2V_SEM()
        self._N2V_RGB = N2V_RGB()
        self._flywing = None

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
        self._segmentation = Segmentation()

    @property
    def denoising(self) -> Denoising:
        return self._denoising
    
    @property
    def segmentation(self) -> Segmentation:
        return self._segmentation

    def __str__(self) -> str:
        return f"Portfolio:\nDenoising datasets: {self.denoising.list_datasets()}\nSegmentation datasets: {self.segmentation.list_datasets()}"
        f""
