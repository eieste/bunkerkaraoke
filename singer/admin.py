from django.contrib import admin
from singer.models import *
# Register your models here.


class SingerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Singer, SingerAdmin)


class SingerSongAdmin(admin.ModelAdmin):
    pass

admin.site.register(SingerSong, SingerSongAdmin)