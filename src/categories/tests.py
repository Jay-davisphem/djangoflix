from django.test import TestCase
from categories.models import Category
from playlists.models import Playlist

class CategoryTestCase(TestCase):
    def setUp(self):
        self.cat_a = Category.objects.create(title="Action")
        self.cat_b = Category.objects.create(title="Comedy", active=False)
        self.play_a = Playlist.objects.create(title="Squid Game", category=self.cat_a)

    def test_is_active(self):
        self.assertTrue(self.cat_a.active)

    def test_not_active(self):
        self.assertFalse(self.cat_b.active)
    def test_related_playlist(self):
        self.assertEqual(self.cat_a.playlists.all().count(), 1)
