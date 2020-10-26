from typing import List
from dataclasses import dataclass

from pydantic import BaseModel


class SimpleSong(BaseModel):
    title: str
    album: str
    artist: str
    year: int


class Image(BaseModel):
    height: int
    url: str
    width: int


class Album(BaseModel):
    id: str
    images: List[Image]
    href: str
    name: str
    release_date: str
    uri: str


class Artist(BaseModel):
    id: str
    href: str
    name: str
    uri: str


class Track(BaseModel):
    album: Album
    artists: List[Artist]
    duration_ms: int
    id: str
    preview_url: str
    uri: str
    name: str
