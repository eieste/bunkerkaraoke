# Generated by Django 5.0.6 on 2024-06-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0003_gameday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameday',
            name='genre',
        ),
        migrations.AddField(
            model_name='gameday',
            name='genres',
            field=models.ManyToManyField(blank=True, to='moderator.genre'),
        ),
        migrations.AlterField(
            model_name='gameday',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='moderator.attribute'),
        ),
        migrations.AlterField(
            model_name='gameday',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gameday',
            name='scheduled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]