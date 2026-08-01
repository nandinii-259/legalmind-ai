from app.rag.generator import GeminiGenerator
from app.rag.retriever import Retriever


class ChatService:

    def __init__(self):
        self.retriever = Retriever()
        self.generator = GeminiGenerator()

    def ask(self, question: str):

        # Retrieve relevant chunks
        results = self.retriever.retrieve(question)

        documents = results["documents"][0]
        metadata = results["metadatas"][0]

        # Build context for Gemini
        context = "\n\n".join(documents)

        # Generate answer
        answer = self.generator.generate(
            question=question,
            context=context,
        )

        # Remove duplicate document names
        seen = set()
        formatted_sources = []

        for item in metadata:

            source = item["source"]

            if source not in seen:

                formatted_sources.append(
                    {
                        "document": source,
                    }
                )

                seen.add(source)

        return {
            "answer": answer,
            "sources": formatted_sources,
        }

    