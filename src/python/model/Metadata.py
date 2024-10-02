from dataclasses import dataclass
from datetime import datetime

from src.python.enum.Category import Category
from src.python.enum.TransformerName import TransformerName


@dataclass
class Metadata:
    url: str
    label: Category | None
    transformer_name: TransformerName | None
    transformer_version: str | None
    date: datetime

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "label": self.label,
            "transformer_name": self.transformer_name,
            "transformer_version": self.transformer_version,
            "date": self.date
        }
