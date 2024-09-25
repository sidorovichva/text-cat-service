from fastapi import APIRouter

from src.python.enum.TransformerName import TransformerName
from src.python.factory.TransformerFactory import TransformerFactory
from src.python.model.Metadata import Metadata
from src.python.service.MainService import MainService

router = APIRouter(prefix="/website")


@router.get("/add")
async def add_website(
        text: str,
        metadata: Metadata,
        transformer_name: TransformerName = TransformerName.valhalla
) -> None:

    transformer = TransformerFactory.get_transformer(transformer_name=transformer_name)
    await MainService(transformer).add(text, metadata)
