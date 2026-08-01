from pathlib import Path
import shutil
import uuid

import fitz  # PyMuPDF
from fastapi import HTTPException, UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class DocumentService:
    @staticmethod
    async def save_pdf(file: UploadFile) -> Path:
        """
        Save uploaded PDF and return its file path.
        """

        unique_filename = f"{uuid.uuid4()}_{file.filename}"

        file_path = UPLOAD_DIR / unique_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return file_path

    @staticmethod
    def extract_text(pdf_path: Path) -> str:
        """
        Extract text from a PDF using PyMuPDF.
        """

        try:
            document = fitz.open(pdf_path)

            text = ""

            for page in document:
                text += page.get_text()

            document.close()

            return text.strip()

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to extract text: {str(e)}",
            )