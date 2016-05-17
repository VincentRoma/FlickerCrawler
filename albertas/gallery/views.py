from .models import Album, Picture
from .serializers import AlbumSerializer, PictureSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @list_route()
    def albertas(self, request):
        albertas = Album.objects.filter(is_journee=False)
        serializer = self.get_serializer(albertas, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @list_route()
    def journee(self, request):
        journee = Album.objects.filter(is_journee=True)
        serializer = self.get_serializer(journee, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def pictures(self, request, pk=None):
        album = Album.objects.get(album_id=pk)
        pictures = Picture.objects.filter(album_id=album.id)
        serializer = PictureSerializer(pictures, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
