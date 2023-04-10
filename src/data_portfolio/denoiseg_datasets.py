from enum import IntEnum

from .portfolio_entry import PortfolioEntry


class NoiseLevel(IntEnum):
    N0 = 0
    N10 = 10
    N20 = 20


class DSB2018(PortfolioEntry):

    def __init__(self, noise_level: NoiseLevel = NoiseLevel.N0) -> None:
        super().__init__(
            name="DSB2018",
            url=self._get_url(noise_level),
            file_name=f"DSB2018_n{noise_level.value}.zip",
            md5_hash=self._get_hash(noise_level),
            description="From the Kaggle 2018 Data Science Bowl challenge, the "
            "training and validation sets consist of 3800 and 670 patches "
            "respectively, while the test set counts 50 images.\n"
            "Original data: "
            "https://www.kaggle.com/competitions/data-science-bowl-2018/data",
            license="GPL-3.0",
            citation="Caicedo, J.C., Goodman, A., Karhohs, K.W. et al. Nucleus "
            "segmentation across imaging experiments: the 2018 Data Science "
            "Bowl. Nat Methods 16, 1247-1253 (2019). "
            "https://doi.org/10.1038/s41592-019-0612-7",
            files={
                "train": ["train_data.npz"],
                "test": ["test_data.npz"],
            },
        )

        # remember noise level
        self._noise_level = noise_level

    @staticmethod
    def _get_url(noise: NoiseLevel) -> str:
        if noise == NoiseLevel.N0:
            return 'https://zenodo.org/record/5156969/files/DSB2018_n0.zip?download=1'
        elif noise == NoiseLevel.N10:
            return 'https://zenodo.org/record/5156977/files/DSB2018_n10.zip?download=1'
        else:
            return 'https://zenodo.org/record/5156983/files/DSB2018_n20.zip?download=1'

    @staticmethod
    def _get_hash(noise: NoiseLevel) -> str:
        if noise == NoiseLevel.N0:
            return "80513b1eda8e08df1d8dcc5543ad1ad1"
        elif noise == NoiseLevel.N10:
            return "aa16c116949d8b8cd573d7bbeacbd0c3"
        else:
            return "81abc17313582a4f04f501e3dce1fe88"

    @property
    def noise_level(self) -> NoiseLevel:
        return self._noise_level


class SegFlywing(PortfolioEntry):

    def __init__(self, noise: NoiseLevel = NoiseLevel.N0) -> None:
        super().__init__(
            name="Flywing",
            url=self._get_url(noise),
            file_name=f"Flywing_n{noise.value}.zip",
            md5_hash=self._get_hash(noise),
            description="This dataset consist of 1428 training and 252 "
            "validation patches of a membrane labeled fly wing. The test set "
            "is comprised of 50 additional images.",
            license="CC BY-SA 4.0",
            citation="Buchholz, T.O., Prakash, M., Schmidt, D., Krull, A., Jug, "
            "F.: Denoiseg: joint denoising and segmentation. In: European "
            "Conference on Computer Vision (ECCV). pp. 324–337. Springer (2020) 8, 9",
            files={
                "train": ["train_data.npz"],
                "test": ["test_data.npz"],
            },
        )

        # remember noise level
        self._noise_level = noise

    @staticmethod
    def _get_url(noise: NoiseLevel) -> str:
        if noise == NoiseLevel.N0:
            return 'https://zenodo.org/record/5156991/files/Flywing_n0.zip?download=1'
        elif noise == NoiseLevel.N10:
            return 'https://zenodo.org/record/5156993/files/Flywing_n10.zip?download=1'
        else:
            return 'https://zenodo.org/record/5156995/files/Flywing_n20.zip?download=1'
        
    @staticmethod
    def _get_hash(noise: NoiseLevel) -> str:
        if noise == NoiseLevel.N0:
            return "09e0af44f0f9862abae3816d7069604a"
        elif noise == NoiseLevel.N10:
            return "64d5300073e02c9651ec88c368c302e8"
        else:
            return "b8fbb96026bd10fd034b8c1270f6edbb"
        

class MouseNuclei(PortfolioEntry):

    def __init__(self, noise: NoiseLevel = NoiseLevel.N0) -> None:
        super().__init__(
            name="MouseNuclei",
            url=self._get_url(noise),
            file_name=f"MouseNuclei_n{noise.value}.zip",
            md5_hash=self._get_hash(noise),
            description="A dataset depicting diverse and non-uniformly "
            "clustered nuclei in the mouse skull, consisting of 908 training "
            "and 160 validation patches. The test set counts 67 additional images",
            license="CC BY-SA 4.0",
            citation="Buchholz, T.O., Prakash, M., Schmidt, D., Krull, A., Jug, "
            "F.: Denoiseg: joint denoising and segmentation. In: European "
            "Conference on Computer Vision (ECCV). pp. 324–337. Springer (2020) 8, 9",
            files={
                "train": ["train_data.npz"],
                "test": ["test_data.npz"],
            },
        )

        # remember noise level
        self._noise_level = noise

    @staticmethod
    def _get_url(noise: NoiseLevel) -> str:
        if noise == NoiseLevel.N0:
            return 'https://zenodo.org/record/5157001/files/Mouse_n0.zip?download=1'
        elif noise == NoiseLevel.N10:
            return 'https://zenodo.org/record/5157003/files/Mouse_n10.zip?download=1'
        else:
            return 'https://zenodo.org/record/5157008/files/Mouse_n20.zip?download=1'
        
    @staticmethod
    def _get_hash(noise: NoiseLevel) -> str:
        if noise == NoiseLevel.N0:
            return "b747d013cba186a02c97937acef4b972"
        elif noise == NoiseLevel.N10:
            return "0b0776fa205057b49920b0ec3d1a5fc9"
        else:
            return "6e9d895ba3ac2c225883ed3ec94342f8"
        