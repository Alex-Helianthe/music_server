from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from infra import APIInfra

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permettre les requêtes depuis tous les domaines. Tu peux restreindre cela à une liste d'origines spécifiques.
    allow_credentials=True,
    allow_methods=["*"],  # Permettre toutes les méthodes HTTP (POST, GET, etc.)
    allow_headers=["*"],  # Permettre tous les headers
)


class SoundBody(BaseModel):
    level: int


@app.post("/sound")
def set_sound_level(body: SoundBody):
    APIInfra.volume_controller.set_volume(body.level)


@app.get("/")
def get_index():
    return FileResponse('./public/index.html')

