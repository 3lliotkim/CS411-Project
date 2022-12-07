import json
import requests

from track import Track
from playlist import Playlist


class SpotifyClient:
    def __init__(self, authorization_token, user_id):
        self.authorization_token = authorization_token
        self.user_id = user_id

    def get_last_played_tracks(self, limit):
        url = f"https://open.spotify.com/collection/tracks"
        response = self._place_get_api_request(url)
        reponse_json = response.json()
        tracks = [Track(track["Track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for 
        track in reponse_json["items"]]

        return tracks
        
