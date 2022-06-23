from django.utils import timezone
from django.utils.text import slugify
from .models import PublishStateOptions


def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_publish = instance.state == PublishStateOptions.PUBLISH
    is_draft = instance.state == PublishStateOptions.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    else:
        instance.publish_timestamp = None


def slugify_pre_save(sender, instance, *args, **kwargs):
    slug = instance.slug
    if not slug:
        instance.slug = slugify(instance.title)
