import pandas as pd
from fastapi import UploadFile


class CSVService:
    """
    Service responsible for loading CSV files.
    """

    async def read_csv(self, file: UploadFile) -> pd.DataFrame:
        return pd.read_csv(file.file)