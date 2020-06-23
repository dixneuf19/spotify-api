import logging
from typing import List

import spotipy
from dotenv import load_dotenv
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from spotipy import SpotifyClientCredentials

from src.models import Track
from src.utils import dict_to_track

load_dotenv()


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = FastAPI()


@app.get("/search")
async def search(q: str) -> Track:
    res = sp.search(q, limit=1, offset=0, type="track")
    if len(res["tracks"]["items"]) > 0:
        return dict_to_track(res["tracks"]["items"][0])
        
    return JSONResponse(
            content=jsonable_encoder({}), status_code=status.HTTP_404_NOT_FOUND
        )

@app.get("/health")
async def get_health():
    return {"message": "OK"}
