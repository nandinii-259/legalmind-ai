from app.rag.embeddings import EmbeddingModel


class EmbeddingService:

    def __init__(self):
        self.model = EmbeddingModel()

    def generate_embeddings(self, chunks: list[str]):

        return [
            self.model.embed(chunk)
            for chunk in chunks
        ]