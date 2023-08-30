# 🎶 PlaylistPasss 🎶
---

- Creator: João Pedro Longo Zucoloto
- Email: joaozuco@gmail.com
- [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-pedro-longo-zucoloto-169638182/)

---

### This project was developed for "copying" playlists from Spotify to YouTube (for now...)

### How to Use
---

### Spotify Client Setup:
1. Create an app on [Spotify for Developers](https://developer.spotify.com).
2. Copy your _client_id_ and _client_secret_.
3. Paste the keys in the _.env_ file.
4. From your Spotify account, copy your _username_ or _user_id_.
5. Paste the _username_ or _user_id_ on line 34 in the "run.py" file
6. The code will then generate a valid token with every run.

### YouTube Headers Setup:
1. Go to [YoutubeMusic](https://music.youtube.com/library).
2. Press F12 to access the _Inspector_.
3. In the _Inspector_, go to the _network_ option, which is the fourth option at the top.
4. Click on the name of any matching request.
5. In the _Headers_ tab, scroll down to the _Request headers_ section and copy the Cookie.
6. Paste your copied value into the "Cookie" key in the _auth/browser.json_ file.

### Running the Code
1. Open the file run.py.
2. Write your Spotify username on line 30.
3. Write the playlist you want to copy on line 31.