# Generated by Django 5.0.6 on 2024-06-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0002_remove_singer_song_singer_gameday_singersong'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]