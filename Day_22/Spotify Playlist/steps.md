### **Step 1: Input the Date**

**What happens in this step:**

- The program asks you to input a date in the format `YYYY-MM-DD`. This date determines the Billboard Hot 100 chart you want to fetch.

**How it works:**

- The input function (`input("Which year do you want to travel to? ...")`) collects the date as a string.
- This string is appended to the base Billboard URL (`https://www.billboard.com/charts/hot-100/`) to construct the full URL for the specific date.

**Why this step is important:**

- Billboard publishes weekly Hot 100 charts, and each date corresponds to a specific week's chart.
- Your input date ensures the program fetches the correct webpage containing the song data.

**Example:**

- If you input `2010-05-10`, the program constructs the URL:
  ```
  https://www.billboard.com/charts/hot-100/2010-05-10
  ```
- This URL is used to scrape the Billboard chart for that specific week.

---

### **Step 2: Web Scraping Billboard**

**What happens in this step:**

- The program sends an HTTP GET request to the constructed URL to fetch the webpage content.
- It uses the `requests` library to make the HTTP request.
- The HTML response is passed to `BeautifulSoup`, which parses it into a format that allows easy extraction of the song names.

**Detailed Workflow:**

1. **Constructing the Request:**

   - The `requests.get()` function sends a GET request to the Billboard URL.
   - A custom `header` is included in the request to mimic a real browser. This avoids potential issues with the website blocking automated tools (web scrapers).
     ```
     header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
     ```

2. **Handling the Response:**

   - If the request is successful (status code 200), the HTML content of the page is stored in the variable `billboard`.
   - If the request fails (e.g., due to network issues or an invalid URL), the program informs you with an error message.

3. **Parsing the HTML:**

   - The HTML content is passed to BeautifulSoup (`soup = BeautifulSoup(billboard, "html.parser")`), which allows you to navigate and search the HTML tree.

4. **Extracting Song Names:**
   - The program searches the HTML structure to locate the song names.
   - This is done using the `.select()` method with the appropriate CSS selector:
     ```
     song_name_tags = soup.select("li h3#title-of-a-story.c-title")
     ```
   - This targets `<h3>` elements with the ID `title-of-a-story` and the class `c-title`, located within `<li>` elements.

**Why this step is important:**

- This is where the Billboard song data is fetched and prepared for further processing. Without this step, the program would not have the list of top songs to create the Spotify playlist.

**Example Output:**

- If successful, the program extracts the song names and prints them:
  ```
  ['Song 1', 'Song 2', 'Song 3', ...]
  ```

### Step 3: **Create a New Playlist**

This step involves creating a Spotify playlist in your account using Spotipy.

1. **Retrieve Your Spotify User ID**:

   - Use `sp.current_user()["id"]` to get your unique Spotify user ID. This ID is required to associate the playlist with your account.

   ```python
   user_id = sp.current_user()["id"]
   ```

2. **Create the Playlist**:

   - Use the `sp.user_playlist_create()` method to create a new playlist.
   - Parameters:
     - `user`: Your Spotify user ID.
     - `name`: The name of the playlist (e.g., "Billboard Hot 100 - YYYY-MM-DD").
     - `public`: `False` means the playlist is private.

   ```python
   playlist = sp.user_playlist_create(
       user=user_id,
       name=f"Billboard Hot 100 - {date}",
       public=False
   )
   ```

3. **Retrieve the Playlist ID**:

   - Spotify returns metadata about the playlist, including its unique `id`, which you’ll need to add tracks later.

   ```python
   playlist_id = playlist["id"]
   ```

---

### Step 4: **Search Songs and Add to Playlist**

This step involves searching for the scraped songs on Spotify and adding them to the created playlist.

1. **Search for Each Song**:

   - Use `sp.search()` to find each song on Spotify.
   - Parameters:
     - `q`: The song name (search query).
     - `type`: `"track"` specifies that you're searching for songs.
     - `limit`: The maximum number of results (set to `1` for the first match).
   - Example:

     ```python
     result = sp.search(q=song, type="track", limit=1)
     ```

   - `result` contains metadata about the search results. The URI (Unique Resource Identifier) of the song is extracted if the song is found:

     ```python
     track_uris.append(result["tracks"]["items"][0]["uri"])
     ```

2. **Handle Missing Songs**:

   - If a song isn’t found on Spotify, `IndexError` will occur. Use a `try-except` block to skip these songs gracefully:

     ```python
     try:
         track_uris.append(result["tracks"]["items"][0]["uri"])
     except IndexError:
         print(f"Song '{song}' not found on Spotify.")
     ```

3. **Add Songs to Playlist**:

   - Once all song URIs are collected, use `sp.playlist_add_items()` to add them to the playlist.
   - Parameters:

     - `playlist_id`: The ID of the playlist created in Step 3.
     - `items`: A list of track URIs.

     ```python
     sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
     ```

4. **Confirmation**:

   - After adding tracks, print a confirmation message indicating how many tracks were successfully added:

     ```python
     print(f"Playlist created successfully with {len(track_uris)} tracks.")
     ```

---

### Example Workflow:

- Scrape the song names: `["Song1", "Song2", "Song3"]`.
- Search Spotify for each song and retrieve URIs: `["spotify:track:123", "spotify:track:456", "spotify:track:789"]`.
- Create a playlist: `"Billboard Hot 100 - YYYY-MM-DD"`.
- Add the retrieved songs to the playlist.

---

### Key Notes:

- Spotify tracks are identified by unique URIs. Without these, you can’t add tracks to a playlist.
- Spotipy handles the interaction with Spotify’s Web API, so all actions (search, create playlist, add songs) are API calls.
- Ensure you handle exceptions (e.g., missing songs) to avoid breaking the script.
