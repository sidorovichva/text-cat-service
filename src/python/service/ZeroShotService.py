import logging

from src.python.transformer.Transformer import Transformer


class ZeroShotService:

    def __init__(self, transformer: Transformer):
        self.__transformer = transformer

    @property
    def transformer(self) -> Transformer:
        return self.__transformer

    async def classify(self, text: str) -> str:

        await self.transformer.download()

        logging.info(f"Classifying text using {self.transformer.short_name}")

        category: str = self.transformer.classify(text)

        return category
