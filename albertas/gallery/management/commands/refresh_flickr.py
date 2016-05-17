from django.core.management.base import BaseCommand, CommandError
from gallery.models import Album, Picture
import flickrapi
from albertas.settings import API_KEY, API_SECRET

class Command(BaseCommand):
    help = 'Refresh flickr database'


    def handle(self, *args, **options):
        #PERSIST ALBERTAS PICTURES
        albums_albertas = self.get_albertas()
        for album in albums_albertas:
            alb, created = Album.objects.get_or_create(**album)
            pictures = self.get_pictures(alb)
        #PERSIST JOURNEE PICTURES
        albums_journee = self.get_journee()
        for album in albums_journee:
            alb, created = Album.objects.get_or_create(**album)
            pictures = self.get_pictures(alb)


    def get_albertas(self):
        flickr = flickrapi.FlickrAPI(API_KEY, API_SECRET, format='parsed-json')
        sets = flickr.photosets.getList(user_id='134304585@N06')
        albums_albertas = []
        for album in sets['photosets']['photoset']:
            if 'Plante' not in album['title']['_content']:
                alb = {
                    'title': album['title']['_content'],
                    'farm': album['farm'],
                    'album_id': album['id'],
                    'nb_pictures': album['photos'],
                    'primary': album['primary'],
                    'secret': album['secret'],
                    'server': album['server'],
                    'is_journee': False
                }
                albums_albertas.append(alb)
        return albums_albertas

    def get_journee(self):
        flickr = flickrapi.FlickrAPI(API_KEY, API_SECRET, format='parsed-json')
        sets = flickr.photosets.getList(user_id='134304585@N06')
        albums_journee = []
        for album in sets['photosets']['photoset']:
            if 'Plante' in album['title']['_content']:
                alb = {
                    'title': album['title']['_content'],
                    'farm': album['farm'],
                    'album_id': album['id'],
                    'nb_pictures': album['photos'],
                    'primary': album['primary'],
                    'secret': album['secret'],
                    'server': album['server'],
                    'is_journee': True
                }
                albums_journee.append(alb)
        return albums_journee

    def get_pictures(self, album):
        flickr = flickrapi.FlickrAPI(API_KEY, API_SECRET, format='parsed-json')
        sets = flickr.photosets.getPhotos(photoset_id='{}'.format(album.album_id), user_id='134304585@N06')
        pictures = []

        for picture in sets['photoset']['photo']:
            pic = {
                'title': picture['title'],
                'farm': picture['farm'],
                'photo_id': picture['id'],
                'secret': picture['secret'],
                'server': picture['server'],
                'album': album
            }
            pict, created = Picture.objects.get_or_create(**pic)
            pictures.append(pict)
        return pictures;
