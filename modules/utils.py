import difflib
import re


class Utils:

    @staticmethod
    async def find_most_compatible_result(yt_search_results, s_track):
        pattern = r'\([^)]*\)'
        s_track_name = s_track['name']
        s_artists = " ".join([a['name'].strip() for a in s_track['artists']]) if s_track['artists'] else ''
        s_album = re.sub(pattern, '', s_track['album']['name'])
        keep_score = []

        for result in yt_search_results[0:11]:
            if result['category'] == 'Songs':

                yt_track = result['title']
                yt_artists = " ".join([a['name'].strip() for a in result['artists']]) if result['artists'] else ''
                yt_album = re.sub(pattern, '', result['album']['name'] if result.get('album') else '')
                yt_id = result['videoId']

                song_similarity = difflib.SequenceMatcher(None, yt_track, s_track_name).ratio()
                artist_similarity = difflib.SequenceMatcher(None, yt_artists, s_artists).ratio()
                album_similarity = difflib.SequenceMatcher(None, yt_album, s_album).ratio()

                keep_score.append(
                    {
                        "spotify_track": s_track_name, "spotify_artists": s_artists, "spotify_album": s_album,
                        "yt_track": yt_track, "yt_artists": yt_artists, "yt_album": yt_album, "yt_id": yt_id,
                        "score": (0.2 * song_similarity) + (0.5 * artist_similarity) + (0.8 * album_similarity)
                    }
                )
        sorted_data = sorted(keep_score, key=lambda x: x['score'], reverse=True)
        return sorted_data[0]['yt_id']
