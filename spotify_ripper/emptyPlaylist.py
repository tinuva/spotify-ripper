import spotipy.util as util
import spotipy.client
import os

#redirect_uri = 'http://www.purple.com'
#client_id = ''
#client_secret = ''
scope = 'playlist-modify-public playlist-modify-private playlist-read-collaborative'

playlist = os.environ["playlist"]
username = os.environ["user"]
client_id = os.environ["SPOTIPY_CLIENT_ID"] 
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]
#print('Spotipy authentication')

#token = None
#spotInstance = None
token = util.prompt_for_user_token(username, scope)
spotInstance = spotipy.Spotify(auth=token)
spotInstance.trace = False

def remove_all_from_playlist(username, playlistURI):
    tracks = get_playlist_tracks(username, playlistURI)
    print ("removing tracks")
    track_ids = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
        tid = track['id']
        track_ids.append(tid)
    results = spotInstance.user_playlist_remove_all_occurrences_of_tracks(username, rPlaylistID, track_ids)

def get_playlist_tracks(username, playlistURI):
    global rPlaylistID
    p1, p2, p3, p4, rPlaylistID = playlistURI.split(':', 5)

    #global token 
    #token = util.prompt_for_user_token(username, scope)

    global spotInstance 
    #spotInstance = spotipy.Spotify(auth=token)
    #spotInstance.trace = False

    print('Getting Results')
    results = spotInstance.user_playlist(username, rPlaylistID, fields="tracks,next")

    tracks = results['tracks']

    return tracks

def main():
  print("cleaning up..")
  remove_all_from_playlist(username, playlist)

if __name__ == "__main__":
    main()