from qdrant_client import QdrantClient as Qdrant


class QdrantClient:

    client = Qdrant(host="localhost", port=6333)

    @classmethod
    def get_client(cls) -> Qdrant:
        return Qdrant(host="localhost", port=6333)
