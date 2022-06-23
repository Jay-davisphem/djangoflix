from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from djangoflix.db.models import PublishStateOptions
from djangoflix.db.receivers import publish_state_pre_save, slugify_pre_save


class VideoQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            state=PublishStateOptions.PUBLISH, publish_timestamp__lte=timezone.now()
        )


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Video(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=225, unique=True)
    active = models.BooleanField(default=True)
    publish_timestamp = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(
        max_length=2,
        choices=PublishStateOptions.choices,
        default=PublishStateOptions.DRAFT,
    )
    objects = VideoManager()

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.state == PublishStateOptions.PUBLISH

    def get_playlist_ids(self):
        return list(self.playlist_featured.all().values_list("id", flat=True))


class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Video"
        verbose_name_plural = "Videos"


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Published Video"
        verbose_name_plural = "Published Videos"


pre_save.connect(publish_state_pre_save, sender=Video)

pre_save.connect(slugify_pre_save, sender=Video)
