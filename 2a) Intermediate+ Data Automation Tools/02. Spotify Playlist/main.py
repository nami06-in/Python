import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}/"
session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.billboard.com/'
}
response = session.get(url=BILLBOARD_URL, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]
# by default strip() removes white spaces and new line


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private",
                                               cache_path="token.txt",
                                               username=os.environ["SPOTIFY_USERNAME"]))

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
