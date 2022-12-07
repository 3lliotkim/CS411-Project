from flask import Flask, render_template, Response, request, redirect, url_for
#from boston_weather import temperature, windspeed, cloud, percipitation, sunny
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
cid = "spotify client id"
secret = "spotify secret id"

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
def get_playlist(creator, id):
    properties = ["artist","album","track_name"]
    playlist_df = pd.DataFrame(columns = properties)
    playlist = sp.user_playlist_tracks(creator, id)["items"]
    playlist_features = {}
    for track in playlist:
        
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)

    return playlist_df[:11]

print(get_playlist('spotify', '37i9dQZF1DWSqBruwoIXkA'))