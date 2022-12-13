import os

from generate_playlist import get_playlist
from spotifyclient import SpotifyClient


def main():


    # get recommended tracks based off seed track
    num_tracks_to_visualise = int(input("How many tracks would you like to visualise? "))
    last_played_tracks = get_playlist("Carrieee", "5osdpIUDfEX7et3SBhLUEJ")

    print(f"\nHere are the last {num_tracks_to_visualise} tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index+1}- {track}")

    indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated by a space: ")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]

    recommended_tracks = SpotifyClient.get_track_recommendations(seed_tracks)
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")


   

    # get playlist name from user and create playlist
    playlist_name = input("\nWhat's the playlist name? ")
    playlist = SpotifyClient.create_playlist(playlist_name)
    print(f"\nPlaylist '{playlist.name}' was created successfully.")

    # populate playlist with recommended tracks
    SpotifyClient.populate_playlist(playlist, recommended_tracks)
    print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")


if __name__ == "__main__":
    main()