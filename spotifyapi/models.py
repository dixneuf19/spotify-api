from typing import List, Optional, Dict
from dataclasses import dataclass

from pydantic import BaseModel


class SimpleSong(BaseModel):
    title: str
    album: str
    artist: str
    year: int


class Image(BaseModel):
    height: Optional[int]
    url: str
    width: Optional[int]


class Album(BaseModel):
    external_urls: Dict[str, str]
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    uri: str


class Artist(BaseModel):
    external_urls: Dict[str, str]
    href: str
    id: str
    name: str
    uri: str


class Track(BaseModel):
    album: Album
    artists: List[Artist]
    duration_ms: int
    external_urls: Dict[str, str]
    href: str
    id: str
    name: str
    preview_url: Optional[str]
    uri: str
