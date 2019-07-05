from rest_framework import serializers

from movies.models import Genre,Movies


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(required=False)
    title = serializers.CharField(required=False)
    rating = serializers.FloatField(required=False)
    rating_count = serializers.IntegerField(required=False)

    class Meta:
        model = Movies
        fields = ['id', 'genre', 'title', 'rating', 'rating_count']


class MovieSerializer1(serializers.ModelSerializer):
    rating = serializers.FloatField(required=True)
    genre = GenreSerializer(required=False)
    title = serializers.CharField(required=False)
    rating_count = serializers.IntegerField(required=False)

    class Meta:
        model = Movies
        fields = ['id', 'genre', 'title', 'rating', 'rating_count']

