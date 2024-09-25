import logging

from src.python.enum.TransformerName import TransformerName
from src.python.transformer.Transformer import Transformer
from src.python.transformer.ValhallaTransformer import ValhallaTransformer


class TransformerFactory:

    @classmethod
    def get_transformer(cls, transformer_name: str) -> Transformer:
        match transformer_name:
            case TransformerName.valhalla:
                return ValhallaTransformer()
            case _:
                message: str = f"Unknown transformer name: {transformer_name}"
                logging.error(message)
                raise ValueError(message)
