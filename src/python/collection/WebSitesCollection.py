from qdrant_client.http.models import CollectionInfo, VectorParams, Distance

from src.python.config.QdrantClient import QdrantClient


class WebSitesCollection:

    client = QdrantClient.get_client()

    collection_name = "websites"
    vector_size = 512

    @classmethod
    def collection_exists(cls, client, collection_name):
        try:
            info = client.get_collection(collection_name)
            return isinstance(info, CollectionInfo)
        except Exception as e:
            return False

    if not collection_exists(client, collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=512, distance=Distance.COSINE),
        )
        print(f"Collection '{collection_name}' created.")
    else:
        print(f"Collection '{collection_name}' already exists.")
