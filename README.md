# Spotify API

[![Test](https://github.com/dixneuf19/SpotifyAPI/workflows/Test/badge.svg)](https://github.com/dixneuf19/SpotifyAPI/actions?query=workflow%3ATest) [![Build and release](https://github.com/dixneuf19/SpotifyAPI/workflows/Build%20and%20release/badge.svg)](https://github.com/dixneuf19/SpotifyAPI/actions?query=workflow%3A"Build+and+release") [![CodeQL](https://github.com/dixneuf19/SpotifyAPI/workflows/CodeQL/badge.svg)](https://github.com/dixneuf19/SpotifyAPI/actions?query=workflow%3ACodeQL)


Yet another wrapper around this API...

## Local development

You can build the *Docker* image with `make build` and then run it with `make run`.

The app is available at <http://localhost:8000>.

## Create k8s secret

Add your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET tokens into your `.env` file for development (**don't commit this file**).

Then you can create the secret with `kubectl create secret generic spotify-api-access --from-env-file=.env`.
