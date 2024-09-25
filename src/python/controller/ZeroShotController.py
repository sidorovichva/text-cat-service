import logging

from fastapi import APIRouter

from src.python.enum.TransformerName import TransformerName
from src.python.factory.TransformerFactory import TransformerFactory
from src.python.service.ZeroShotService import ZeroShotService

router = APIRouter(prefix="/classifier")


@router.get("/zero_shot")
async def zero_shot_classifier(
        text: str,
        transformer_name: TransformerName = TransformerName.valhalla
) -> str:

    logging.info(f"Classifying text: {text}")

    transformer = TransformerFactory.get_transformer(transformer_name=transformer_name)

    category: str = await ZeroShotService(transformer).classify(text)
    return category
