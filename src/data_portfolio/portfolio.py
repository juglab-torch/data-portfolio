from pathlib import Path
from dataclasses import dataclass
from enum import IntEnum
from typing import Union


class Denoising():
    """
    """

    def __init__(self):	
        self._N2V_BSD64 = N2V_BSD64()
        self._N2V_SEM = N2V_SEM()
        self._N2N_SEM = None
        self._RGB = N2V_RGB()
        self._flywing = Flywing()
        self._DSB2018 = None

    @property
    def N2V_BSD64(self):
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
        return ["N2V_BSD", "SEM", "RGB", "flywing", 'DSB2018']  


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

    def download(self, path: Union[str, Path], create_parents: bool = True) -> dict:
        """Download the dataset to the given path.

        Args:
            path (Union[str, Path]): Path in which the data should be downloaded
            create_parents (bool, optional): Create parent directories if they don't exist. Defaults to True.

        Returns:
            dict: A dictionnary containing path to the different files or folders.
        """
        pass

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
            link="https://download.fht.org/jug/n2v/SEM.zip",
            description=
                "Cropped images from a SEM dataset from T.-O. Buchholz et al "
                "(Methods Cell Biol, 2020).",
            license="CC-BY",
            citation=
                "T.-O. Buchholz, A. Krull, R. Shahidi, G. Pigino, G. Jékely, "
                "F. Jug, \"Content-aware image restoration for electron "
                "microscopy\", Methods Cell Biol 152, 277-289"
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

class Flywing(PortfolioEntry):
    def __init__(self):
        super().__init__(
            name="N2V_flywing",
            link="https://download.fht.org/jug/n2v/flywing-data.zip",
            description=
                "Flywing 3D dataset from T.-O. Buchholz et al (Methods Cell Biol, "
                "2020).",
            license="CC-BY",
            citation=
                "T.-O. Buchholz, A. Krull, R. Shahidi, G. Pigino, G. Jékely, "
                "F. Jug, \"Content-aware image restoration for electron "
                "microscopy\", Methods Cell Biol 152, 277-289."
        )


class DSB2018(PortfolioEntry):
    
    class NoiseLevel(IntEnum):
        N0 = 0
        N10 = 10
        N20 = 20
    
    def __init__(self, noise_level: NoiseLevel = NoiseLevel.N0):
        super().__init__(
            name="DSB2018",
            link=f"https://zenodo.org/record/5156969/files/DSB2018_n"
                "{noise_level.value}"
                ".zip?download=1",
            description=
                "From the Kaggle 2018 Data Science Bowl challenge, the "
                "training and validation sets consist of 3800 and 670 patches "
                "respectively, while the test set counts 50 images.\n"
                "Original data: "
                "https://www.kaggle.com/competitions/data-science-bowl-2018/data",
            license="GPL-3.0",
            citation=
            "Caicedo, J.C., Goodman, A., Karhohs, K.W. et al. Nucleus "
            "segmentation across imaging experiments: the 2018 Data Science "
            "Bowl. Nat Methods 16, 1247–1253 (2019). "
            "https://doi.org/10.1038/s41592-019-0612-7"
        )

        # remember noise level
        self._noise_level = noise_level