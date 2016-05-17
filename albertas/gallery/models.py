from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)
    farm = models.IntegerField()
    album_id = models.CharField(max_length=50)
    nb_pictures = models.IntegerField()
    primary = models.CharField(max_length=50)
    secret = models.CharField(max_length=50)
    server = models.CharField(max_length=50)
    is_journee = models.BooleanField(default=False)


class Picture(models.Model):
    photo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    farm = models.IntegerField()
    secret = models.CharField(max_length=50)
    server = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
