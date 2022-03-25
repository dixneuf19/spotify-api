from fastapi.testclient import TestClient

from spotifyapi.main import app

client = TestClient(app)

queries_responses = {
    "logical song supertramp": {
        "album": {
            "external_urls": {
                "spotify": "https://open.spotify.com/album/1zcm3UvHNHpseYOUfd0pna"
            },
            "href": "https://api.spotify.com/v1/albums/1zcm3UvHNHpseYOUfd0pna",
            "id": "1zcm3UvHNHpseYOUfd0pna",
            "images": [
                {
                    "height": 640,
                    "url": "https://i.scdn.co/image/ab67616d0000b2735405ef9e393f5f1e53b4b42e",
                    "width": 640,
                },
                {
                    "height": 300,
                    "url": "https://i.scdn.co/image/ab67616d00001e025405ef9e393f5f1e53b4b42e",
                    "width": 300,
                },
                {
                    "height": 64,
                    "url": "https://i.scdn.co/image/ab67616d000048515405ef9e393f5f1e53b4b42e",
                    "width": 64,
                },
            ],
            "name": "Breakfast In America (Deluxe Edition)",
            "release_date": "1979-03-29",
            "uri": "spotify:album:1zcm3UvHNHpseYOUfd0pna",
        },
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/3JsMj0DEzyWc0VDlHuy9Bx"
                },
                "href": "https://api.spotify.com/v1/artists/3JsMj0DEzyWc0VDlHuy9Bx",
                "id": "3JsMj0DEzyWc0VDlHuy9Bx",
                "name": "Supertramp",
                "uri": "spotify:artist:3JsMj0DEzyWc0VDlHuy9Bx",
            }
        ],
        "duration_ms": 251253,
        "external_urls": {
            "spotify": "https://open.spotify.com/track/6mHOcVtsHLMuesJkswc0GZ"
        },
        "href": "https://api.spotify.com/v1/tracks/6mHOcVtsHLMuesJkswc0GZ",
        "id": "6mHOcVtsHLMuesJkswc0GZ",
        "name": "The Logical Song - Remastered 2010",
        "preview_url": None,
        "uri": "spotify:track:6mHOcVtsHLMuesJkswc0GZ",
    },
    'album:"logical song" year:1979': {
        "album": {
            "external_urls": {
                "spotify": "https://open.spotify.com/album/0qut6VWFY5AYVROlB3BdzZ"
            },
            "href": "https://api.spotify.com/v1/albums/0qut6VWFY5AYVROlB3BdzZ",
            "id": "0qut6VWFY5AYVROlB3BdzZ",
            "images": [
                {
                    "height": 640,
                    "url": "https://i.scdn.co/image/ab67616d0000b2736cd022a1650af9d88f2499b4",
                    "width": 640,
                },
                {
                    "height": 300,
                    "url": "https://i.scdn.co/image/ab67616d00001e026cd022a1650af9d88f2499b4",
                    "width": 300,
                },
                {
                    "height": 64,
                    "url": "https://i.scdn.co/image/ab67616d000048516cd022a1650af9d88f2499b4",
                    "width": 64,
                },
            ],
            "name": "The Logical Song",
            "release_date": "1979-03-01",
            "uri": "spotify:album:0qut6VWFY5AYVROlB3BdzZ",
        },
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/3JsMj0DEzyWc0VDlHuy9Bx"
                },
                "href": "https://api.spotify.com/v1/artists/3JsMj0DEzyWc0VDlHuy9Bx",
                "id": "3JsMj0DEzyWc0VDlHuy9Bx",
                "name": "Supertramp",
                "uri": "spotify:artist:3JsMj0DEzyWc0VDlHuy9Bx",
            }
        ],
        "duration_ms": 249731,
        "external_urls": {
            "spotify": "https://open.spotify.com/track/5AsHmx17yMs3BRqga0eSby"
        },
        "href": "https://api.spotify.com/v1/tracks/5AsHmx17yMs3BRqga0eSby",
        "id": "5AsHmx17yMs3BRqga0eSby",
        "name": "The Logical Song",
        "preview_url": "https://p.scdn.co/mp3-preview/aa7c3cc49f5b2b4b38062bb9bbe4dc4c1073cf76?cid=e96e446ccf954386b7c25e97a6015728",
        "uri": "spotify:track:5AsHmx17yMs3BRqga0eSby",
    },
}

simple_queries_responses = {
    "logical song supertramp": {
        "album": "Breakfast In America (Deluxe Edition)",
        "year": 1979,
        "artist": "Supertramp",
        "title": "The Logical Song - Remastered 2010",
        "external_urls": {
            "spotify": "https://open.spotify.com/track/6mHOcVtsHLMuesJkswc0GZ"
        },
    },
    'album:"logical song" year:1979': {
        "album": "The Logical Song",
        "year": 1979,
        "artist": "Supertramp",
        "title": "The Logical Song",
        "external_urls": {
            "spotify": "https://open.spotify.com/track/5AsHmx17yMs3BRqga0eSby"
        },
    },
}


def test_search_logical_song():
    response = client.get("/search", params={"q": "logical song supertramp"})
    assert response.status_code == 200
    assert response.json() == queries_responses["logical song supertramp"]


def test_search_logical_song_simple():
    response = client.get(
        "/search", params={"q": "logical song supertramp", "simple": True}
    )
    assert response.status_code == 200
    assert response.json() == simple_queries_responses["logical song supertramp"]


def test_search_with_filters():
    response = client.get("/search", params={"q": 'album:"logical song" year:1979'})
    assert response.status_code == 200
    assert response.json() == queries_responses['album:"logical song" year:1979']


def test_search_with_filters_simple():
    response = client.get(
        "/search", params={"q": 'album:"logical song" year:1979', "simple": True}
    )
    assert response.status_code == 200
    assert response.json() == simple_queries_responses['album:"logical song" year:1979']


def test_search_with_wrong_param():
    response = client.get("/search", params={"query": "logical song supertramp"})
    assert response.status_code == 422


def test_search_non_existing_track():
    response = client.get("/search", params={"q": "no song named like this for sure"})
    assert response.status_code == 404


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
