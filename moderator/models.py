from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.title}"


class AttributeKey(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class Attribute(models.Model):
    key = models.ForeignKey(AttributeKey, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.key}: {self.value}"

class Interpret(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    attributes = models.ManyToManyField(Attribute)
    interpret = models.ForeignKey(Interpret, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class GameDay(models.Model):
    current = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    #attributes = models.ManyToManyField(Attribute, blank=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        if self.current is False:
            if self.scheduled_at is not None:
                if self.scheduled_at > timezone.now():
                    return "Planned at"+self.scheduled_at
                else:
                    return "Ausgelaufen"
            return "Regular Gameday"
        else:
            return "Heutiger GameDay"