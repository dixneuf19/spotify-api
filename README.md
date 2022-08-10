# Spotify API

[![TestS](https://github.com/dixneuf19/SpotifyApi/actions/workflows/test.yaml/badge.svg)](https://github.com/dixneuf19/SpotifyApi/actions/workflows/test.yaml) [![CD](https://github.com/dixneuf19/SpotifyApi/actions/workflows/build-and-release.yaml/badge.svg)](https://github.com/dixneuf19/SpotifyApi/actions/workflows/build-and-release.yaml)


Yet another wrapper around this API...

## Local development

You can build the *Docker* image with `make build` and then run it with `make run`.

Or you can simply launch in you correct Python environment with `make dev`.

The app is available at <http://localhost:8000>.

## Create k8s secret

Add your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET tokens into your `.env` file for development (**don't commit this file**).

Then you can create the secret on Kubernetes with `kubectl create secret generic spotify-api-access --from-env-file=.env`.
