from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'realease_date')
    search_fields = ('id', 'title', 'genre', 'realease_date')
