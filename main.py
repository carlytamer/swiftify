import spotipy
import pandas
import matplotlib
from spotipy.oauth2 import SpotifyClientCredentials

taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(taylor_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])