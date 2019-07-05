from users.models import UserProfile
from users.serializers import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # user = UserProfile.objects.get(id=self.user.id)
    # movies = user.movies
    # movies = movies + request.movie
    # user.update(movies=movies)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FavMov(APIView):
    def get(self, pk):
        try:
            user = UserProfile.objects.get(id=pk)
        except UserProfile.DoesNotExist as e:
            return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = UserProfile.objects.get(id=pk)
        serializer = UserSerializer(user)
        if serializer.is_valid():
            serializer.save()
            movies = user.movies
            movies = movies + request.data.pop('movies')
            user.update(movies=movies)
            return Response(serializer.data)
        return Response(serializer.errors)

