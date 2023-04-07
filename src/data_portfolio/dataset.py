from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Denoising():
    """
    """

    def __init__(self):	
        self._N2V_BSD = N2V_BSD64()
        self._N2V_SEM = N2V_SEM()
        self._RGB = Denoising.RGB
        self._flywing = Denoising.flywing

    @property
    def BSD64(self):
        return self._N2V_BSD64

    @property
    def N2V_SEM(self):
        return self._N2V_SEM
    
    @property
    def RGB(self):
        return self._RGB
    
    @property
    def flywing(self):
        return self._flywing
    

    @classmethod
    def list_datasets(cls) -> list[str]:
        return ["N2V_BSD", "SEM", "RGB", "flywing"]



@dataclass
class Portfolio():
    denoising: Denoising


@dataclass
class PortfolioEntry():
    name: str
    link: str
    description: str
    license: str
    citation: str



class N2V_BSD64(PortfolioEntry):
    def __init__(self):
        super().__init__(
            name="N2V_BSD64",
            link="https://download.fht.org/jug/n2v/BSD68_reproducibility.zip",
            description=
                "This dataset is taken from K. Zhang et al (TIP, 2017). \n"
                "It consists of 400 gray-scale 180x180 images (cropped from the "
                "BSD dataset) and splitted between training and validation, and "
                "68 gray-scale test images (BSD68).\n"
                "All images were corrupted with Gaussian noise with standard "
                "deviation of 25 pixels. The test dataset contains the uncorrupted "
                "images as well.\n"
                "Original dataset: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/",
            license="Unknown",
            citation=
                "D. Martin, C. Fowlkes, D. Tal and J. Malik, \"A database of "
                "human segmented natural images and its application to "
                "evaluating segmentation algorithms and measuring ecological "
                "statistics,\" Proceedings Eighth IEEE International "
                "Conference on Computer Vision. ICCV 2001, Vancouver, BC, "
                "Canada, 2001, pp. 416-423 vol.2, doi: "
                "10.1109/ICCV.2001.937655.",
        )

class N2V_SEM(PortfolioEntry):
    def __init__(self):
        super().__init__(
            name="N2V_SEM",
            link="https://download.fht.org/jug/n2v/RGB.zip",
            description=
                "",
            license="CC-BY",
            citation=
                ""
        )

class N2V_RGB(PortfolioEntry):
    def __init__(self):
        super().__init__(
            name="N2V_RGB",
            link="https://download.fht.org/jug/n2v/RGB.zip",
            description=
                "Banner of the CVPR 2019 conference with extra noise.",
            license="CC0",
            citation=
                "A. Krull, T.-O. Buchholz and F. Jug, \"Noise2Void - Learning "
                "Denoising From Single Noisy Images,\" 2019 IEEE/CVF "
                "Conference on Computer Vision and Pattern Recognition (CVPR),"
                " 2019, pp. 2124-2132"
        )

