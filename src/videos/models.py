from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        # CONSTANT = DB_VALUE, USER_DISPLAY_VALUE
        PUBLISH = "PU", "Published"
        DRAFT = "DR", "Draft"
        UNLISTED = "UN", "Unlisted"
        PRIVATE = "PR", "Private"

    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=225, unique=True)
    active = models.BooleanField(default=True)
    publish_timestamp = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(
        max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT
    )
    # publish_timestamp

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.state == self.VideoStateOptions.PUBLISH

    def save(self, *args, **kwargs):
        if (
            self.state == self.VideoStateOptions.PUBLISH
            and self.publish_timestamp is None
        ):
            print("Save as timestamp for published")
            self.publish_timestamp = timezone.now()
        else:
            self.publish_timestamp = None
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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
