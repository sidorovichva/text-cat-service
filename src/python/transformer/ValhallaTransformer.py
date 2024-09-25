import logging
import os

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from src.python.Utils import Utils
from src.python.enum.Category import Category
from src.python.enum.TransformerName import TransformerName
from src.python.transformer.Transformer import Transformer


class ValhallaTransformer(Transformer):

    def __init__(self):
        super().__init__(
            short_name=TransformerName.valhalla,
            name="valhalla/distilbart-mnli-12-1",
            folder='valhalla'
        )

    async def download(self) -> None:
        if (
                not os.path.exists(self.path())
                or Utils.is_directory_empty(self.model_path())
                or Utils.is_directory_empty(self.tokenizer_path())
        ):
            logging.info(f"Downloading {self.short_name} transformer")

            tokenizer = AutoTokenizer.from_pretrained(self.name)
            tokenizer.save_pretrained(self.tokenizer_path())

            model = AutoModelForSequenceClassification.from_pretrained(self.name)
            model.save_pretrained(self.model_path())

    def classify(self, text: str) -> str:
        tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_path())
        model = AutoModelForSequenceClassification.from_pretrained(self.model_path())

        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits

        probs = torch.softmax(logits, dim=-1)

        predicted_label = torch.argmax(probs, dim=-1).item()

        labels = [c for c in Category]

        return labels[predicted_label]
