from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Movies(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movie')
    title = models.CharField(max_length=255)
    rating = models.FloatField(default=1, validators=[MinValueValidator(0), MaxValueValidator(10)])
    rating_count = models.IntegerField(default=1)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    @property
    def avg_rating(self):
        return self.rating

    def __str__(self):
        return f'{self.id}: {self.title}'


