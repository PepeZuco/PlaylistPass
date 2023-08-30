import asyncio
from modules.spotify import Spotify
from modules.youtube_music import YoutubeMusic
from modules.utils import Utils

sp = Spotify()
ytm = YoutubeMusic()


async def spotify_to_youtube_music_async(s_usrename,
                                         s_playlist_from,
                                         yt_new_playlist_name,
                                         yt_new_playlist_description):
    s_playlist_id = await sp.get_playlist_id(s_usrename, s_playlist_from)
    s_tracks = await sp.get_playlist_data_by_id(s_playlist_id)
    yt_playlist_id = await ytm.create_playlist(yt_new_playlist_name, yt_new_playlist_description)
    yt_tracks_to_be_added = []

    tasks = []

    for s_track in s_tracks:
        yt_search_results = await ytm.search_tracks(s_track)
        task = asyncio.create_task(Utils.find_most_compatible_result(yt_search_results, s_track))
        tasks.append(task)

    yt_tracks_to_be_added = await asyncio.gather(*tasks)

    await ytm.add_song_to_playlist(yt_playlist_id, yt_tracks_to_be_added)
    return yt_playlist_id


async def main():
    try:
        SPOTIFY_USERNAME = 'SPOTIFY_USERNAME'
        SPOTIFY_PLAYLIST_FROM = 'SPOTIFY_PLAYLIST_FROM'
        YOUTUBE_MUSIC_NEW_PLAYLIST_NAME = 'YOUTUBE_MUSIC_NEW_PLAYLIST_NAME'
        YOUTUBE_MUSIC_NEW_PLAYLIST_DESCRIPTION = 'YOUTUBE_MUSIC_NEW_PLAYLIST_DESCRIPTION'
        playlist_id = await spotify_to_youtube_music_async(s_usrename=SPOTIFY_USERNAME,
                                                           s_playlist_from=SPOTIFY_PLAYLIST_FROM,
                                                           yt_new_playlist_name=YOUTUBE_MUSIC_NEW_PLAYLIST_NAME,
                                                           yt_new_playlist_description=YOUTUBE_MUSIC_NEW_PLAYLIST_DESCRIPTION)
        print('-' * (len(playlist_id) + 5))
        print(f'https://music.youtube.com/playlist?list={playlist_id}')
        print('-' * (len(playlist_id) + 5))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
