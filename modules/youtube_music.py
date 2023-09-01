import os
import googleapiclient.discovery
from ytmusicapi import YTMusic
from typing import List, Dict


class YoutubeMusic:
    def __init__(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyAwy1zjc4Ap4OZauCp5AiosqCm57uutOlE"
        self.youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
        self.ytmusic = YTMusic('auth/browser.json')

    async def get_user_playlist_data(self, channelId: str) -> List[Dict[str, str]]:
        request = self.youtube.playlists().list(
            part="snippet,contentDetails",
            channelId=channelId,
            maxResults=100
        )
        response = request.execute()
        print('YoutubeMusic - Searching playlists')

        result = []
        for r in response['items']:
            result.append({
                'id': r['id'],
                'name': r['snippet']['title'],
                'n_tracks': r['contentDetails']['itemCount']
            })

        print('YoutubeMusic - Found playlist')
        return result

    async def get_playlist_by_id(self, playlist_id: str) -> List[Dict[str, str]]:
        request = self.youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=100,
            playlistId=playlist_id)
        response = request.execute()
        print('YoutubeMusic - Getting playlist data')

        result = []
        for r in response['items']:
            parsed = r['snippet']['description'].split('\n')
            track_data = parsed[2].split('·')
            result.append({
                'track_id': r['id'],
                'name': track_data[0].strip(),
                'artists': track_data[1].strip(),
                'album': parsed[4]
            })
        print('YoutubeMusic - Got playlist data')
        return result

    async def get_id_from_tracks(self, playlist_id: str, n_tracks: int) -> List[Dict[str, str]]:
        request = self.youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=n_tracks,
            playlistId=playlist_id)
        response = request.execute()
        print('YoutubeMusic - Getting playlist tracks id')

        result = [r['contentDetails']['videoId'] for r in response['items']]
        print('YoutubeMusic - Got playlist data')
        return result

    async def create_playlist(self, name: str, description: str) -> List[Dict[str, str]]:
        request = self.ytmusic.create_playlist(name, description)
        print('YoutubeMusic - Created YoutubeMusic playlist')
        return request

    async def add_song_to_playlist(self, playlist: str, track_id: str) -> List[Dict[str, str]]:
        self.ytmusic.add_playlist_items(playlist, track_id)
        print('YoutubeMusic - Added songs to playlist')

    async def search_tracks(self, s_tracks: dict) -> List[Dict]:
        track_name = s_tracks['name']
        track_album = s_tracks['album']['name']
        track_artists = " ".join([a['name'].strip() for a in s_tracks['artists']])

        print('YoutubeMusic - Searching tracks')
        return self.ytmusic.search(query=f'{track_name} {track_album} {track_artists}', filter='songs')
