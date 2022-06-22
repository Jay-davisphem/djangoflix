from django.contrib import admin

from .models import VideoAllProxy, VideoPublishedProxy


class VideoAllProxyAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "state", "video_id", "is_published"]
    search_fields = ["title"]
    readonly_fields = ["id", "is_published", "publish_timestamp"]
    list_filter = ["state", "active"]

    class Meta:
        model = VideoAllProxy


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ["title", "video_id"]
    search_fields = ["title"]
    # list_filter = ['video_id']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)


admin.site.register(VideoAllProxy, VideoAllProxyAdmin)
admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
