from typing import Dict, Any

from src.models import Artist, Image, Album, Track


def dict_to_track(obj: Dict[str,Any]) -> Track:
    try:
        return Track(
            album=dict_to_album(obj["album"]),
            artists=[dict_to_artist(art) for art in obj["artists"]],
            duration_ms=obj["duration_ms"],
            id=obj["id"],
            preview_url=obj["preview_url"],
            uri=obj["uri"],
            name=obj["name"],
        )
    except KeyError:
        return None


def dict_to_image(obj: Dict[str,Any]) -> Image:
    try:
        return Image(height=obj["height"], url=obj["url"], width=obj["width"],)
    except KeyError:
        return None


def dict_to_album(obj: Dict[str,Any]) -> Album:
    try:
        return Album(
            id=obj["id"],
            images=[dict_to_image(img) for img in obj["images"]],
            href=obj["href"],
            name=obj["name"],
            release_date=obj["release_date"],
            uri=obj["uri"],
        )
    except KeyError:
        return None


def dict_to_artist(obj: Dict[str,Any]) -> Artist:
    try:
        return Artist(
            id=obj["id"], href=obj["href"], name=obj["name"], uri=obj["uri"],
        )
    except KeyError:
        return None
