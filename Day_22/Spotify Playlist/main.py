import os
import requests
from bs4 import BeautifulSoup
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

# Step 1: Scrape Billboard Top 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Adding headers for the HTTP request
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# URL for the Billboard Hot 100 chart of the given date
URL = "https://www.billboard.com/charts/hot-100/" + date

# Sending the GET request
response = requests.get(url=URL, headers=header)

# Checking if the response is successful
if response.status_code != 200:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
else:
    # Parsing the webpage content
    billboard = response.text
    soup = BeautifulSoup(billboard, "html.parser")

    # Extracting song names by targeting the unique parent structure
    song_name_tags = soup.select("li h3#title-of-a-story.c-title")  # Targets <h3> within <li>

    # Storing song names in a list
    songs = [song.getText().strip() for song in song_name_tags]

    # Printing the result
    if songs:
        print(songs)
    else:
        print("No song names found. Check if the date is valid or the structure has changed.")

# Step 2: Authenticate with Spotify
sp = Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                       client_secret=CLIENT_SECRET,
                                       redirect_uri=REDIRECT_URI,
                                       scope="playlist-modify-private"))

# Step 3: Create a new Playlist
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Hot-100 {date}", public=False)
playlist_id = playlist["id"]

# Search Songs and Add to Playlist
track_uris = []

for song in songs:
    result = sp.search(q=song, type="track", limit=1)
    try:
        track_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} not found in Spotify")

# Add tracks to the playlist
if track_uris:
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
    print(f"Playlist created successfully with {len(track_uris)} tracks.")
else:
    print("No tracks added to the playlist.")
