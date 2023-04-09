import hashlib
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Union
from urllib import request

from tqdm import tqdm


# from https://stackoverflow.com/a/53877507
class DownloadProgressBar(tqdm):
    def update_to(self, b: float = 1, bsize: float = 1, tsize: float = None) -> None:
        if tsize is not None:
            self.total = tsize
            self.update(b * bsize - self.n)


@dataclass
class PortfolioEntry:
    name: str
    url: str
    description: str
    license: str
    citation: str
    file_name: str
    md5_hash: str
    files: dict[str, list]

    def download(
        self,
        path: Union[str, Path],
        check_md5: bool = True,
        create_parents: bool = True,
    ) -> dict:
        """Download dataset to the given path.

        Args:
        ----
            path (Union[str, Path]): Folder in which the data should be downloaded
            create_parents (bool, optional): Create parent directories if they don't exist. Defaults to True.

        Returns:
        -------
            dict: A dictionnary containing path to the different files or folders.
        """
        path = Path(path)
        if path.exists() and not path.is_dir():
            raise ValueError(f"Path {path} is not a directory.")

        if not path.exists():
            path.mkdir(parents=create_parents)

        # check if zip file exists
        zip_path = Path(path, self.file_name)
        if not zip_path.exists():
            # download and unzip data
            print(f"Downloading {self.name} to {path} might take some time.")
            with DownloadProgressBar(
                unit="MB", unit_scale=True, miniters=1, desc=self.url.split("/")[-1]
            ) as t:
                request.urlretrieve(self.url, filename=zip_path, reporthook=t.update_to)
            print("Download finished.")

        # check if md5 hash is correct
        if check_md5:
            print(f"Checking MD5 hash of {zip_path}.")
            hash = hashlib.md5(open(zip_path, "rb").read()).hexdigest()
            if hash != self.md5_hash:
                raise ValueError(
                    f"MD5 hash of {zip_path} is not correct. Expected {self.md5_hash}, got {hash}."
                )
            print("MD5 hash is correct.")

        # check if data has been unzipped before
        data_path = Path(path, self.name[:-4])
        # TODO progress bar
        print(f"Unzipping {zip_path} to {data_path}.")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(data_path)
        print("Unzipping finished.")

        # TODO create dictionnary with paths to files
        return self.files
