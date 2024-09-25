from fastapi import FastAPI

from src.python.controller import ZeroShotController

app = FastAPI()
app.include_router(ZeroShotController.router)
