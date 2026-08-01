from pathlib import Path
import shutil
import uuid

from fastapi import HTTPException, UploadFile

from app.rag.chunking import TextChunker
from app.services.embedding_service import EmbeddingService
from app.services.pdf_service import PDFService
from app.services.vector_store_service import VectorStoreService

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class DocumentService:

    def __init__(self):
        self.pdf_service = PDFService()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.vector_store_service = VectorStoreService()

    async def process_pdf(self, file: UploadFile) -> dict:

        unique_filename = f"{uuid.uuid4()}_{file.filename}"

        file_path = UPLOAD_DIR / unique_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        try:

            text, page_count = self.pdf_service.extract_text(file_path)

            chunks = self.chunker.split(text)

            embeddings = self.embedding_service.generate_embeddings(
                chunks
            )

            self.vector_store_service.store(
                chunks=chunks,
                embeddings=embeddings,
                filename=unique_filename,
            )

            file_size = file_path.stat().st_size / (1024 * 1024)

            return {
                "message": "PDF uploaded successfully.",
                "filename": unique_filename,
                "file_size": f"{file_size:.2f} MB",
                "page_count": page_count,
                "character_count": len(text),
                "chunk_count": len(chunks),
            }

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e),
            )