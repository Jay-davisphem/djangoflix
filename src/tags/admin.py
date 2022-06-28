from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from .models import TaggedItem


class TaggedItemInline(GenericTabularInline):
    model = TaggedItem
    extra = 0


@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
    fields = ["tag", "content_type", "object_id", "content_object"]
    readonly_fields = ["tag", "content_type", "object_id", "content_object"]

    class Meta:
        model = TaggedItem
