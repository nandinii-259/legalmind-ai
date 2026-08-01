from pathlib import Path
import shutil
import uuid

import fitz
from fastapi import HTTPException, UploadFile

from app.rag.chunking import TextChunker
from app.rag.embeddings import GeminiEmbedding
from app.rag.vector_store import VectorStore

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class DocumentService:

    def __init__(self):
        self.chunker = TextChunker()
        self.embedding_model = GeminiEmbedding()
        self.vector_store = VectorStore()

    async def process_pdf(self, file: UploadFile) -> dict:
        """
        Complete PDF processing pipeline:
        Save → Extract → Chunk → Embed → Store
        """

        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = UPLOAD_DIR / unique_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        try:
            document = fitz.open(file_path)

            text = ""

            for page in document:
                text += page.get_text()

            page_count = document.page_count

            document.close()

            text = text.strip()

            chunks = self.chunker.split(text)

            embeddings = []

            for chunk in chunks:
                embedding = self.embedding_model.embed(chunk)
                embeddings.append(embedding)

            self.vector_store.add_chunks(
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
                detail=f"Failed to process PDF: {str(e)}",
            )