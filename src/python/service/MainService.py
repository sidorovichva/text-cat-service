from src.python.model.Metadata import Metadata
from src.python.service.QdrantService import QdrantService
from src.python.service.VectorizationService import VectorizationService
from src.python.transformer.Transformer import Transformer


class MainService:

    def __init__(self, transformer: Transformer):
        self.__transformer = transformer

    @property
    def transformer(self) -> Transformer:
        return self.__transformer

    async def add(self, text: str, metadata: Metadata):

        await self.transformer.download()

        vector: list[str] = VectorizationService.vectorize(text)

        category: str = self.transformer.classify(text)

        metadata.category = category
        metadata.transformer_name = self.transformer.short_name
        metadata.transformer_version = "1"

        QdrantService.add(vector, metadata, category)




