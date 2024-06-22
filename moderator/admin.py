from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib import admin
from moderator.models import *


class SongAdmin(admin.ModelAdmin):
    pass
    list_display = ["title", "interpret", "genre"]

admin.site.register(Song, SongAdmin)



class InterpretAdmin(admin.ModelAdmin):
    pass


admin.site.register(Interpret, InterpretAdmin)



class AttributeKeyAdmin(admin.ModelAdmin):
    pass


admin.site.register(AttributeKey, AttributeKeyAdmin)



class AttributeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attribute, AttributeAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre, GenreAdmin)



@admin.action(description=_("Create Regular Gameday"))
def create_regular_gameday(modeladmin, request, queryset):
    GameDay.objects.all().update(current=False)
    GameDay.objects.create(current=True)


class GameDayAdmin(admin.ModelAdmin):
    list_display = ["__str__", "current", "created_at", "scheduled_at", "genre_list"]
    actions = [create_regular_gameday]


    def genre_list(self, object):
        return ", ".join(object.genres.all().values_list("title", flat=True))


admin.site.register(GameDay, GameDayAdmin)


