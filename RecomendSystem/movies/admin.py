from django.contrib import admin
from movies.models import Genre,Movies


@admin.register(Movies)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'rating_count')


admin.site.register(Genre)