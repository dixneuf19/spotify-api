import logging
from typing import List

import spotipy
from dotenv import load_dotenv
from fastapi import FastAPI, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from spotipy import SpotifyClientCredentials

from spotifyapi.models import Track

load_dotenv()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = FastAPI()


@app.get(
    "/search",
    response_model=Track,
    responses={
        404: {
            "description": "No track found for this query",
        },
        200: {"description": "Found a track for this query"},
    },
)
async def search(
    query: str = Query(
        ...,
        title="Search query terms",
        alias="q",
        description="The query you would type in Spotify search bar",
    )
) -> Track:
    res = sp.search(query, limit=1, offset=0, type="track")
    if len(res["tracks"]["items"]) > 0:
        return res["tracks"]["items"][0]

    return JSONResponse(
        content=jsonable_encoder({}), status_code=status.HTTP_404_NOT_FOUND
    )


@app.get("/health")
async def get_health():
    return {"message": "OK"}
