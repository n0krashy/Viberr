from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User


class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    album_cover = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music/detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=150)
    is_favorite = models.BooleanField(default=False)
    audio_file = models.FileField(default='', blank=True)

    def __str__(self):
        return self.song_title
