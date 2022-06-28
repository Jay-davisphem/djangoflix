from django.contrib import admin
from .models import Playlist, PlaylistItem, TVShowProxy, TVShowSeasonProxy, MovieProxy
from tags.admin import TaggedItemInline


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem


class PlaylistAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline, PlaylistItemInline]

    class Meta:
        model = Playlist

    def get_queryset(self, request):
        return Playlist.objects.filter(type=Playlist.PlaylistTypeChoices.PLAYLIST)


admin.site.register(Playlist, PlaylistAdmin)


class SeasonEpisodeInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0


@admin.register(TVShowSeasonProxy)
class TVShowSeasonProxyAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline, SeasonEpisodeInline]
    list_display = ["title", "parent"]

    class Meta:
        model = TVShowSeasonProxy

    def get_queryset(self, request):
        return TVShowSeasonProxy.objects.all()


class TVShowSeasonProxyInline(admin.TabularInline):
    model = TVShowSeasonProxy
    extra = 0
    fields = ["order", "title", "state"]


class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline, TVShowSeasonProxyInline]
    fields = ["title", "category", "description", "state", "video", "slug"]
    list_display = ["title"]
    readonly_fields = ["tags"]

    class Meta:
        model = TVShowProxy

    def get_queryset(self, request):
        return TVShowProxy.objects.all()


admin.site.register(TVShowProxy, TVShowProxyAdmin)


@admin.register(MovieProxy)
class MovieProxyAdmin(admin.ModelAdmin):
    list_display = ["title"]
    fields = ["title", "category", "description", "state", "video", "slug"]
    readonly_fields = ["tags"]

    class Meta:
        model = MovieProxy

    def get_queryset(self, request):
        return MovieProxy.objects.all()
