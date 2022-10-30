#!spotify/Scripts python

import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

from credentials import username, client_id, client_secret, redirect_uri

def get_data(sp, username, file_path, update=False):
    playlists_response = sp.user_playlists(username)
    playlists = playlists_response['items']

    user_playlists = [{playlist['name']: playlist['id']} for playlist in playlists]


    if update:
        with open(file_path, 'w') as f:
            json.dump(user_playlists, f)
        print("Data file updated :)")


    return user_playlists
    

def list_songs(sp, playlist_id):
    songs_response = sp.user_playlist_tracks(playlist_id=playlist_id)
    songs = {}
    song_name = songs_response['items'][0]['track']['name']
    song_id = songs_response['items'][0]['track']['id']
    #items -> [list of tracks] -> track -> name, id etc.
    for track in songs_response['items']:
        song_name = track['track']['name']
        song_id = track['track']['id']
        songs[song_name] =  song_id
    return songs



if __name__ == "__main__":
    scope = 'user-library-read'
    data_path = 'data/playlists.json'

    sp_oauth = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    playlists = get_data(sp, username, data_path, update=True)
    playlist_id = playlists[1]['cunt']
    print(f"{list(playlists[1].keys())[0]}:")
    print(list_songs(sp, playlist_id))

    print("Succesful!")