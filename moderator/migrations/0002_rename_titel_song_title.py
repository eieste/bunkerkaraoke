# Generated by Django 5.0.6 on 2024-06-22 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='titel',
            new_name='title',
        ),
    ]
