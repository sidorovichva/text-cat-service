from qdrant_client import QdrantClient as Qdrant
import os


class QdrantClient:

    client = Qdrant(":memory:") if os.getenv("env") == "dev" else Qdrant(host="localhost", port=6333)

    @classmethod
    def get_client(cls) -> Qdrant:
        return Qdrant(":memory:") if os.getenv("env") == "dev" else Qdrant(host="localhost", port=6333)
