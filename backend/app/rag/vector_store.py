import chromadb

from app.core.config import settings


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name="legalmind_documents"
        )

    def add_chunks(
        self,
        chunks,
        embeddings,
        filename,
    ):

        ids = [
            f"{filename}_{i}"
            for i in range(len(chunks))
        ]

        metadatas = [
            {
                "source": filename,
                "chunk": i,
            }
            for i in range(len(chunks))
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )