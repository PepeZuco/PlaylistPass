# 🎶 PlaylistPasss 🎶
- - - - 
- creator: João Pedro Longo Zucoloto
- [email](joaozuco@gmail.com)
- [linkedin](https://www.linkedin.com/in/jo%C3%A3o-pedro-longo-zucoloto-169638182/)
- - - - 
### This project was developed for "copying" playlists from spotify to youtube (for now...)

### How to use
----
### Spotify client setup:
1 - Create a app on [Spotify for Developers](https://developer.spotify.com)

2 - Copy your _client_id_ and _client_secret_.

3 - Paste the keys in the _.env_ file.

4 - From your Spotify account, copy your _username_ or _user_id_.

5 - Copy the _username_ or _user_id_ one line 12 from "modulos/spotify.py".

6 - From that, the code will generate a valid token for every run.


### Youtube headers setup:
1 - Go to [YoutubeMusic](https://music.youtube.com/library).

2 - Press F12 to acess the _Inspector_.

3 - In the _Inspector_, go to the _network_ option, fourth at the top.

5 - Click on the name of any matching request. 

6 - In the _Headers_ tab, scroll to the section _Request headers_ and copy everything starting from _“accept: */*”_ to the end of the section

7 - Past your values on _auht/youtube_headers_setup.py_ headers_row variable

### Run
1 - Go to file run.py.

2 - Write the playlist on line 7.# PlaylistPass
