import spotify
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
 
cid = '9b5a593955474abfa7bc427fac9cd806'
secret = '부여받은 비밀번호'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)