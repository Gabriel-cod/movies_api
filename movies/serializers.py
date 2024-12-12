from django.db.models import Avg
from rest_framework import serializers
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_realease_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("Movies older than 1990 are not allowed")
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'realease_date', 'resume', 'rate',]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None
