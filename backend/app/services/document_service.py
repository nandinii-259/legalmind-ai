import os
import chromadb
from pypdf import PdfReader
from sqlalchemy.orm import Session

from app.config import UPLOAD_DIR, VECTOR_DB_DIR
from app.models.document import Document
from app.rag.chunking import split_text
from app.rag.embeddings import embedding_model

chroma_client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
collection = chroma_client.get_or_create_collection(name="legal_documents")


def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def process_uploaded_document(file_path: str, filename: str, db: Session) -> dict:
    # Step 1: extract text
    raw_text = extract_text_from_pdf(file_path)
    if not raw_text.strip():
        raise ValueError("No extractable text found in this PDF.")

    # Step 2: chunk the text
    chunks = split_text(raw_text, source=filename)

    # Step 3: generate embeddings for all chunks
    chunk_texts = [c["text"] for c in chunks]
    vectors = embedding_model.embed_documents(chunk_texts)

    # Step 4: store in ChromaDB
    ids = [f"{filename}-{c['chunk_index']}" for c in chunks]
    metadatas = [{"source": c["source"], "chunk_index": c["chunk_index"]} for c in chunks]

    collection.add(
        ids=ids,
        embeddings=vectors,
        documents=chunk_texts,
        metadatas=metadatas,
    )

    # Step 5: record metadata in SQLite
    doc_record = Document(filename=filename, chunk_count=len(chunks))
    db.add(doc_record)
    db.commit()
    db.refresh(doc_record)

    return {
        "document_id": doc_record.id,
        "filename": filename,
        "chunk_count": len(chunks),
    }