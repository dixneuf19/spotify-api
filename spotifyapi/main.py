import logging
from typing import List, Union

import spotipy
from dotenv import load_dotenv
from fastapi import FastAPI, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from spotipy import SpotifyClientCredentials

from spotifyapi.models import SimpleTrack, Track, convert_track_to_simple_track

load_dotenv()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = FastAPI()


@app.get(
    "/search",
    response_model=Union[Track, SimpleTrack],
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
    ),
    simple: bool = Query(
        False,
        title="Require a simple response",
        description="If set to true, return SimpleTrack object",
    ),
) -> Track:
    res = sp.search(query, limit=1, offset=0, type="track")
    if len(res["tracks"]["items"]) == 0:
        return JSONResponse(
            content=jsonable_encoder({}), status_code=status.HTTP_404_NOT_FOUND
        )

    track = Track(**res["tracks"]["items"][0])
    if simple:
        return convert_track_to_simple_track(track)
    return track


@app.get("/health")
async def get_health():
    return {"message": "OK"}
