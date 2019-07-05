from rest_framework import serializers
from django.contrib.auth.models import User

from movies.serializers import MovieSerializer


class UserSerializer(serializers.ModelSerializer):
    # movies = MovieSerializer(many=True, read_only=False)

    class Meta:
        model = User
        fields = ['id','username']