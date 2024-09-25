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
                raise ValueError(f"Unknown transformer name: {transformer_name}")