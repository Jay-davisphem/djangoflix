from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=225)
    active = models.BooleanField(default=True)
    # timestamp
    # updated
    # state
    # publish_timestamp

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        print(self)
        return self.active


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
