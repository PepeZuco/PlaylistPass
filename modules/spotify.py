from dotenv import load_dotenv
import os
import base64
import requests
import json
from typing import List, Dict


class Spotify:
    def __init__(self):
        load_dotenv()
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")

        auth_string = client_id + ":" + client_secret
        auth_bytes = auth_string.encode("ascii")
        auth_base64 = str(base64.b64encode(auth_bytes), "ascii")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"}

        data = {"grant_type": "client_credentials"}
        result = requests.post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        self.token = json_result["access_token"]
        self.auth_header = {"Authorization": "Bearer " + self.token}

    async def get_user_playlist_data(self, username: str) -> List[Dict[str, str]]:
        url = f'https://api.spotify.com/v1/users/{username}/playlists'
        headers = self.auth_header

        r = requests.get(url, headers=headers)
        print('---------------------------------')
        print('Spotify - Searching playlists')
        json_result = json.loads(r.content)

        result = []
        for j in json_result['items']:
            result.append({
                'id': j['id'],
                'name': j['name'],
                'n_tracks': j['tracks']['total']
            })

        print('Spotify - Found playlist')
        return result

    async def get_playlist_data_by_id(self, playlist_id: str) -> List[Dict[str, str]]:
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
        headers = self.auth_header

        r = requests.get(url, headers=headers)
        print('---------------------------------')
        print('Spotify - Getting playlist data')
        json_result = json.loads(r.content)

        result = []
        for j in json_result['tracks']['items']:
            track_id = j['track']['href'].split('/')[5]

            artists = [{'id': a['id'], 'name': a['name']} for a in j['track']['artists']]

            album_artists = [{'id': a['id'], 'name': a['name']} for a in j['track']['album']['artists']]
            album = {
                'id': j['track']['album']['id'],
                'name': j['track']['album']['name'],
                'artists': album_artists
            }

            result.append({
                'track_id': track_id,
                'name': j['track']['name'],
                'artists': artists,
                'album': album
            })
        print('Spotify - Got playlist data')
        return result

    async def get_playlist_id(self, s_username: str, s_playlist_from: str) -> str:
        playlists = await self.get_user_playlist_data(s_username)

        for p in playlists:
            if p['name'] == s_playlist_from:
                return p['id']
