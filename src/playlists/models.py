from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from djangoflix.db.models import PublishStateOptions
from djangoflix.db.receivers import publish_state_pre_save, slugify_pre_save

class PlaylistQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            state=PublishStateOptions.PUBLISH, publish_timestamp__lte=timezone.now()
        )


class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Playlist(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    publish_timestamp = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(
        max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT
    )
    objects = PlaylistManager()

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.state == PublishStateOptions.PUBLISH

pre_save.connect(publish_state_pre_save, sender=Playlist)

pre_save.connect(slugify_pre_save, sender=Playlist)
