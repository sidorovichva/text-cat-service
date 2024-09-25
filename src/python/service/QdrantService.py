from src.python.config.QdrantClient import QdrantClient
from src.python.model.Metadata import Metadata


class QdrantService:

    @classmethod
    def add(
            cls,
            vector: list[str],
            metadata: Metadata,
            collection: str
    ) -> None:
        client = QdrantClient.get_client()
        max_size: int = 100
        length: int = len(vector)
        client.add(
            collection_name=collection,
            documents=vector,
            metadata=metadata.to_dict(),
            ids=[max_size, length]
        )
