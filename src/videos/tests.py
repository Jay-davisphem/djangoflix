from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import Video


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.a = Video.objects.create(title="Kiniun Ololaju", video_id="abc")
        self.b = Video.objects.create(
            title="Kiniun Ololaju",
            state=Video.VideoStateOptions.PUBLISH,
            video_id="123",
        )

    def test_slug_field(self):
        title = self.a.title
        text_slug = slugify(title)
        print(text_slug)
        self.assertEqual(text_slug, self.a.slug)

    def test_valid_title(self):
        title = "Kiniun Ololaju"
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_count(self):
        title = "Kiniun Ololaju"
        qs = Video.objects.filter(title=title)
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.PUBLISH)
        now = timezone.now()
        pu_qs = qs.filter(publish_timestamp__lte=now)
        self.assertTrue(pu_qs.exists())
