from django.test import TestCase

from .models import Video

class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='Kiniun Ololaju')

    def test_valid_title(self):
        title = 'Kiniun Ololaju'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
    
    def test_count(self):
        title = 'Kiniun Ololaju'
        qs = Video.objects.filter(title=title)
        self.assertEqual(qs.exists(), 1)
