import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
cid = "SPOTIFY CLIENT ID"
secret = "SPOTIFY SECRET ID"
client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
def get_playlist(creator, id):
    properties = ["Artist","Album","Song"]
    playlist_df = pd.DataFrame(columns = properties)
    playlist = sp.user_playlist_tracks(creator, id)["items"]
    playlist_features = {}
    for track in playlist:
        playlist_features["Artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["Album"] = track["track"]["album"]["name"]
        playlist_features["Song"] = track["track"]["name"]
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
    return playlist_df[:31]

