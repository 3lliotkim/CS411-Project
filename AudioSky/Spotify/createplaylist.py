import os

from spotifyclient  import SpotifyClient

def main():

    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"), os.getenv("SPOTIFY_USER_ID"))
    num_tracks_to_visualise = int(input("how many tracks do you want to visualise?"))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)


    print(f"Here are the last {num_tracks_to_visualise} tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index +1}- {track}")


    indexes = input("Enter a list of up to 5 tracks ")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]


    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("Here we go: ")
    for index, track in enumerate(recommended_tracks):
        print(f"{index +1}- {track}")

    playlist_name = input("what's the playlist name ? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"Playlist '{playlist_name}' was created successfully.")

    spotify_client.populate_playlist(playlist, recommended_tracks)


if __name__ == "__main__":
    main

