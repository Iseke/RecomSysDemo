from django.http import Http404

from movies.models import Genre, Movies
from movies.serializers import GenreSerializer, MovieSerializer, MovieSerializer1

from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class SetRating(APIView):
    def get_movie(self, request, pk1, pk2):
        try:
            movies = Genre.objects.get(id=pk1).movie.get(id=pk2)
        except:
            raise Http404
        return movies

    def put(self, request, pk1, pk2):
        movie = self.get_movie(request, pk1, pk2)
        try:
            request.data.pop('genre')
        except:
            pass
        serializer = MovieSerializer1(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            movie.rating_count += 1
            movie.rating = (request.data.pop('rating')+movie.avg_rating)/movie.rating_count
            movie.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MovieDetail(APIView):
    def get_movie(self, request, pk1, pk2):
        try:
            movies = Genre.objects.get(id=pk1).movie.get(id=pk2)
        except:
            raise Http404
        return movies

    def get(self, request, pk1, pk2):
        movie1 = self.get_movie(request,pk1, pk2)
        serializer = MovieSerializer(movie1)
        return Response(serializer.data)

    def put(self, request, pk1, pk2):
        movie = self.get_movie(request, pk1, pk2)
        try:
            request.data.pop('genre')
        except:
            pass
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk1, pk2):
        movie = self.get_movie(request, pk1, pk2)
        movie.delete()
        return Response({"delete_status": "successful"})
