import json
import requests

from track import Track
from playlist import Playlist


class SpotifyClient:
    def __init__(self, authorization_token, user_id):
        self.authorization_token = authorization_token
        self.user_id = user_id

    def get_last_played_tracks(self, limit):
        url = f"https://api.spotify.com/v1/tracks"
        response = self._place_get_api_request(url)
        reponse_json = response.json()
        tracks = [Track(track["Track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for 
        track in reponse_json["items"]]

        return tracks
        
    def get_track_recommendations(self, seed_tracks, limit+50):
        seed_tracks_url =""
        for see_track in seed_tracks:
            seed_track_url += see_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}" 
        response =  self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for 
            track in response_json["tracks"] ]
        return tracks

    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Recommend tracks",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response =  self._place_get_api_request(url, data)
        response_json = response,json()

        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return Playlist
    
    
    def populate_playlist(self, playlist, tracks):
        tracks_uris = [Track.create_spotify_uri() for track in tracks]
        data = json.dumps(tracks_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = self._place_get_api_request(url, data)
        response_json = response.json()
        return response_json






    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data = data,
            headers ={
                "Content-Type": "application/json",
                "Authorization": f"Bearer{self.authorization_token}"
            }

        )



    def _place_get_api_request(self, url):
        response = response.get(
            url,
            headers ={
                "Content-Type": "application/json",
                "Authorization": f"Bearer{self.authorization_token}"
            }
                
                )
            
        return response
