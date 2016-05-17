from .models import Album, Picture
from rest_framework import serializers

# Serializers define the API representation.
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
