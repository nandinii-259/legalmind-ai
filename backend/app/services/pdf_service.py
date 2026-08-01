from pathlib import Path
import fitz
from fastapi import HTTPException


class PDFService:

    @staticmethod
    def extract_text(pdf_path: Path) -> tuple[str, int]:

        try:
            document = fitz.open(pdf_path)

            text = ""

            for page in document:
                text += page.get_text()

            page_count = document.page_count

            document.close()

            return text.strip(), page_count

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to process PDF: {str(e)}",
            )