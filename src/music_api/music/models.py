from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=255)
    album_title=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    album_logo=models.CharField(max_length=10000)

    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=20)
    song_title=models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

class Playlist(models.Model):
    Playlist_name=models.CharField(default='',max_length=255)
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('music:detail',kwargs ={'pk':self.pk})
    def __str__(self):
        return self.Playlist_name
