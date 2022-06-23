from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import Playlist
from djangoflix.db.models import PublishStateOptions


class PlaylistModelTestCase(TestCase):
    def setUp(self):
        self.a = Playlist.objects.create(title="Kiniun Ololaju")
        self.b = Playlist.objects.create(
            title="Kiniun Ololaju",
            state=PublishStateOptions.PUBLISH,
        )

    def test_slug_field(self):
        title = self.a.title
        text_slug = slugify(title)
        print(text_slug)
        self.assertEqual(text_slug, self.a.slug)

    def test_valid_title(self):
        title = "Kiniun Ololaju"
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_count(self):
        title = "Kiniun Ololaju"
        qs = Playlist.objects.filter(title=title)
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

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

