from app.rag.vector_store import VectorStore


class VectorStoreService:

    def __init__(self):
        self.vector_store = VectorStore()

    def store(
        self,
        chunks,
        embeddings,
        filename,
    ):
        self.vector_store.add_chunks(
            chunks=chunks,
            embeddings=embeddings,
            filename=filename,
        )