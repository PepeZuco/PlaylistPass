import asyncio
from modules.spotify import Spotify
from modules.youtube_music import YoutubeMusic
from modules.utils import Utils
from collections import Counter


class Tools:
    def __init__(self):
        self.sp = Spotify()
        self.ytm = YoutubeMusic()

    # Spotify
    async def spotify_to_youtube_music(self,
                                       s_usrename: str,
                                       s_playlist_from: str,
                                       yt_new_playlist_name: str,
                                       yt_new_playlist_description: str) -> str:
        s_playlist_id = await self.sp.get_playlist_id(s_usrename, s_playlist_from)
        s_tracks = await self.sp.get_playlist_data_by_id(s_playlist_id)
        yt_playlist_id = await self.ytm.create_playlist(yt_new_playlist_name, yt_new_playlist_description)
        yt_tracks_to_be_added = []

        tasks = []

        for s_track in s_tracks:
            yt_search_results = await self.ytm.search_tracks(s_track)
            task = asyncio.create_task(Utils.find_most_compatible_result(yt_search_results, s_track))
            tasks.append(task)

        yt_tracks_to_be_added = await asyncio.gather(*tasks)

        await self.ytm.add_song_to_playlist(yt_playlist_id, yt_tracks_to_be_added)
        print('-' * (len(yt_playlist_id) + 5))
        print(f'https://music.youtube.com/playlist?list={yt_playlist_id}')
        print('-' * (len(yt_playlist_id) + 5))

    # Youtube Music
    async def create_playlist_youtube_music_most_current_tracks_in_playlists(self, channel_id: str, number_of_most_frequent_songs: int):
        playlist_data = await self.ytm.get_user_playlist_data(channel_id)
        result = [await self.ytm.get_id_from_tracks(p['id'], p['n_tracks']) for p in playlist_data]
        flat_list = [item for sublist in result for item in sublist]

        value_counts = Counter(flat_list)
        most_common_values = value_counts.most_common(number_of_most_frequent_songs)
        tracks_ids = [item[0] for item in most_common_values]

        playlist_id = await self.ytm.create_playlist(f'Top {number_of_most_frequent_songs} most frequent songs in playlists', f'Top {number_of_most_frequent_songs} most frequent songs in playlists')
        await self.ytm.add_song_to_playlist(playlist_id, tracks_ids)
        print('-' * (len(playlist_id) + 5))
        print(f'https://music.youtube.com/playlist?list={playlist_id}')
        print('-' * (len(playlist_id) + 5))
