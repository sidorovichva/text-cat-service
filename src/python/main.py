from fastapi import FastAPI

from src.python.controller import MainController
from src.python.controller import ZeroShotController

app = FastAPI()
app.include_router(ZeroShotController.router)
app.include_router(MainController.router)
