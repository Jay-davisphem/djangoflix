from videos.models import Video
from playlists.models import Playlist

a = Video.objects.create(title="Kiniun Ololaju", video_id="abcabc113")
playlist_a = Playlist.objects.create(title="New Playlist", video=a)
