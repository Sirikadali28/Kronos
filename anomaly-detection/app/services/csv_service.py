from pathlib import Path
import shutil

import pandas as pd
from fastapi import UploadFile


class CSVService:
    """
    Handles CSV upload, storage and loading.
    """

    def __init__(self):
        self.upload_dir = Path("app/storage/uploads")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    async def read_csv(
        self,
        file: UploadFile,
    ) -> pd.DataFrame:
        """
        Read an uploaded CSV directly into a DataFrame.
        """
        return pd.read_csv(file.file)

    async def save_upload(
        self,
        file: UploadFile,
        filename: str,
    ) -> Path:
        """
        Save uploaded CSV to disk.
        """
        destination = self.upload_dir / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return destination

    def load_saved_csv(
        self,
        filepath: Path,
    ) -> pd.DataFrame:
        """
        Load a saved CSV file from disk.
        """
        return pd.read_csv(filepath)