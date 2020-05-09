from typing import List
from dataclasses import dataclass


@dataclass
class SimpleSong:
    title: str
    album: str
    artist: str
    year: int


@dataclass
class Image:
    height: int
    url: str
    width: int


@dataclass
class Album:
    _id: str
    images: List[Image]
    href: str
    name: str
    release_date: str
    uri: str


@dataclass
class Artist:
    _id: str
    href: str
    name: str
    uri: str


@dataclass
class Track:
    album: Album
    artists: List[Artist]
    duration_ms: int
    _id: str
    preview_url: str
    uri: str
