from django.db import models
from moderator.models import Song, GameDay
# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    gameday = models.ForeignKey(GameDay, on_delete=models.CASCADE)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SingerSong(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    accepted = models.BooleanField(default=False)
    planned_order = models.IntegerField()

    def __str__(self):
        return f"{self.song} von {self.singer}"