from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "It's not possible to register reviews with less than 0 stars."),
            MaxValueValidator(5, "It's not possible to register reviews with more than 5 stars."),
        ]
    )
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.movie} - {self.stars}'