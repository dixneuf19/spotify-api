from dataclasses import dataclass
from typing import Dict, List, Optional

from dateparser import parse as date_parse
from pydantic import BaseModel


class SimpleTrack(BaseModel):
    title: str
    album: str
    artist: str
    year: Optional[int]
    external_urls: Dict[str, str] = {}


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


def convert_track_to_simple_track(track: Track) -> SimpleTrack:
    return SimpleTrack(
        title=track.name,
        album=track.album.name,
        artist=track.artists[0].name if len(track.artists) > 0 else "",
        year=date_parse(track.album.release_date).year,
        external_urls=track.external_urls,
    )
