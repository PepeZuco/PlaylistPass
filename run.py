import asyncio
from modules.tools import Tools


async def main():
    try:

        # ========================================================================================================
        # Transfer spotify playlist to Youtube Music.
        # tools = Tools()
        # SPOTIFY_USERNAME = 'USERNAME'
        # SPOTIFY_PLAYLIST_FROM = 'PLAYLIST_FROM'
        # YOUTUBE_MUSIC_NEW_PLAYLIST_NAME = 'YOUTUBE_MUSIC_NEW_PLAYLIST_NAME'
        # YOUTUBE_MUSIC_NEW_PLAYLIST_DESCRIPTION = 'YOUTUBE_MUSIC_NEW_PLAYLIST_DESCRIPTION'
        # await tools.spotify_to_youtube_music(s_usrename=SPOTIFY_USERNAME,
        #                                      s_playlist_from=SPOTIFY_PLAYLIST_FROM,
        #                                      yt_new_playlist_name=YOUTUBE_MUSIC_NEW_PLAYLIST_NAME,
        #                                      yt_new_playlist_description=YOUTUBE_MUSIC_NEW_PLAYLIST_DESCRIPTION)
        # =========================================================================================================

        # =========================================================================================================
        # Create Playlist based on most frequent songs.
        # tools = Tools()
        # CHANNEL_ID = 'YOUR_CHANNEL_ID'
        # await tools.create_playlist_youtube_music_most_current_tracks_in_playlists(channel_id=CHANNEL_ID,
        #                                                                            number_of_most_frequent_songs=50)
        # =========================================================================================================
        pass
    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
