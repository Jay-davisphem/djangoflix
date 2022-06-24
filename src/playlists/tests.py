from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import Playlist
from videos.models import Video
from djangoflix.db.models import PublishStateOptions


class PlaylistModelTestCase(TestCase):
    def create_show_with_seasons(self):
        th_of = Playlist.objects.create(title="The Office")
        s1 = Playlist.objects.create(title="The Office S1", parent=th_of, order=1)
        s2 = Playlist.objects.create(title="The Office S2", parent=th_of, order=2)
        s = Playlist.objects.create(title="The Office S3", parent=th_of, order=3)
        self.show = th_of

    def create_videos(self):
        vid_a = Video.objects.create(title="My tfjkfle", video_id="123abcs")
        vid_b = Video.objects.create(title="My titlfkfjke", video_id="12abc")
        vid_c = Video.objects.create(title="fMffy title", video_id="123asssdbc")
        self.vid_a = vid_a
        self.vid_b = vid_b
        self.vid_c = vid_c
        self.video_qs = Video.objects.all()

    def setUp(self):
        self.create_videos()
        self.create_show_with_seasons()
        self.a = Playlist.objects.create(
            title="Kiniun Ololaju", state=PublishStateOptions.PUBLISH, video=self.vid_a
        )
        self.b = Playlist.objects.create(title="Ajanlekoko", video=self.vid_a)
        self.b.videos.set(self.video_qs)
        self.b.save()

    def test_video_playlist(self):
        qs = self.vid_a.playlist_featured.all()
        self.assertTrue(qs.count(), 2)

    def test_playlist_video_items(self):
        count = self.b.videos.all().count()
        self.assertEqual(count, 3)

    def test_playlist_video_through_model(self):
        vid_qs = sorted(list(self.video_qs.values_list("id")))
        vid_qs2 = sorted(list(self.b.videos.all().values_list("id")))
        playlist_item_qs = sorted(
            list(self.b.playlistitem_set.all().values_list("video"))
        )
        self.assertEqual(vid_qs, vid_qs2, playlist_item_qs)

    def test_playlist_video(self):
        self.assertEqual(self.a.video, self.vid_a)

    def test_video_playlist_ids_properly(self):
        ids = self.a.video.get_playlist_ids()
        act_ids = list(
            Playlist.objects.filter(video=self.vid_a).values_list("id", flat=True)
        )
        self.assertEqual(ids, act_ids)

    def test_slug_field(self):
        title = self.a.title
        text_slug = slugify(title)
        self.assertEqual(text_slug, self.a.slug)

    def test_valid_title(self):
        title = "Kiniun Ololaju"
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_count(self):
        title = "Kiniun Ololaju"
        qs = Playlist.objects.filter(title=title)
        self.assertEqual(qs.count(), 1)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 5)

    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        pu_qs = qs.filter(publish_timestamp__lte=now)
        self.assertTrue(pu_qs.exists())

    def test_publish_manager(self):
        published_qs = Playlist.objects.all().published()
        published_qs_2 = Playlist.objects.published()
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs.count(), published_qs_2.count())

    def test_show_has_seasons(self):
        seasons = self.show.playlist_set.all()
        self.assertTrue(seasons.count() == 3)
