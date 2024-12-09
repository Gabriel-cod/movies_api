from django.db.models import Avg
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return round(rate, 1)
        
        return None
    
    def validate_realease_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("Movies older than 1990 are not allowed")
        return value