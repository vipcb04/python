# Generated by Django 5.1.7 on 2025-03-30 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_artist_user_song_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='song',
            name='uploaded_by',
        ),
    ]
