from abc import abstractmethod, ABC

from src.python.enum.TransformerName import TransformerName


class Transformer(ABC):

    def __init__(self, short_name: TransformerName, name: str, folder: str):
        self.__short_name: TransformerName = short_name
        self.__name: str = name
        self.__folder: str = folder

    @property
    def short_name(self) -> str:
        return self.__short_name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def folder(self) -> str:
        return self.__folder

    @abstractmethod
    async def download(self) -> None:
        pass

    @abstractmethod
    def classify(self, text: str) -> str:
        pass

    @abstractmethod
    def encode(self, text: str) -> list[int]:
        pass

    def path(self) -> str:
        return f"src/resources/transformers/{self.folder}"

    def model_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/model"

    def tokenizer_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/tokenizer"
