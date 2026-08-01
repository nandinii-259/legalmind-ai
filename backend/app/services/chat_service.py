from app.rag.generator import GeminiGenerator
from app.rag.retriever import Retriever


class ChatService:

    def __init__(self):
        self.retriever = Retriever()
        self.generator = GeminiGenerator()

    def ask(self, question: str):

        results = self.retriever.retrieve(question)

        documents = results["documents"][0]

        context = "\n\n".join(documents)

        answer = self.generator.generate(
            question=question,
            context=context,
        )

        return {
            "answer": answer,
            "sources": results["metadatas"][0],
        }