#!spotify/Scripts python

import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pprint as pp

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
    

def list_songs(sp: spotipy.Spotify, playlist_id):
    songs_response = dict(sp.playlist_tracks(playlist_id=playlist_id))
    songs = {}
    song_name = songs_response['items'][0]['track']['name']
    song_id = songs_response['items'][0]['track']['id']
    #items -> [list of tracks] -> track -> name, id etc.
    for track in songs_response['items']:
        song_name = track['track']['name']
        song_id = track['track']['id']
        songs[song_name] =  song_id
    return songs

def get_song_features(sp: spotipy.Spotify, song_ids):
    if len(song_ids) > 1:
        pass
    print(f"Audio features:")
    response = sp.audio_features(song_ids)
    pp.pp(response)

def get_featured_artists(sp: spotipy.Spotify, song_id):
    track = sp.track(song_id)
    artists = {artist['name']: artist['id'] for artist in track['artists']}
    return artists


if __name__ == "__main__":
    scope = 'user-library-read'
    data_path = 'data/playlists.json'

    sp_oauth = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    playlists = get_data(sp, username, data_path, update=True)
    playlist_id = playlists[1]['Listen to this bitch']
    print(f"{list(playlists[1].keys())[0]}:")
    pp.pp(list_songs(sp, playlist_id))
    #get_song_features(sp, ['1njYD38zSElj8PVnTy6G5e'])
    artists = get_featured_artists(sp, '00nlvJd1e6EGFc2dzssl9g')
    print(artists)

    print("Succesful!")