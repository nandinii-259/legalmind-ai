from pathlib import Path
import shutil
import uuid

from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class DocumentService:
    @staticmethod
    async def save_pdf(file: UploadFile) -> str:
        """
        Save uploaded PDF and return the saved filename.
        """

        unique_filename = f"{uuid.uuid4()}_{file.filename}"

        file_path = UPLOAD_DIR / unique_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return unique_filename