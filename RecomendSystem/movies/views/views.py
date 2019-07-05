from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes

from movies.serializers import GenreSerializer, MovieSerializer
from movies.models import Genre, Movies


class getBest(generics.ListAPIView):
    def get_queryset(self):
        return Movies.objects.all();

    def get_serializer_class(self):
        return MovieSerializer


class GenreList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [permission() for permission in (AllowAny,)]
    #     elif self.request.method == 'POST':
    #         return (IsAdminUser, )



class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return AllowAny(),
    #
    #     elif self.request.method in ('PUT', 'DELETE', ):
    #         return IsAdminUser(),


class MovieList(generics.ListCreateAPIView):
    def get_queryset(self):
        genre = get_object_or_404(Genre, id=self.kwargs[self.lookup_field])
        return Movies.objects.filter(genre=genre, )

    def perform_create(self, serializer):
        try:
            genre = Genre.objects.get(id=self.kwargs['pk'])
        except Genre.DoesNotExist:
            raise Http404
        serializer.save(genre=genre)

    serializer_class = MovieSerializer

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return AllowAny(),
    #     elif self.request.method == 'POST':
    #         return IsAdminUser(),
