from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDeleteView, MovieStatsView


urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='create-read-movies'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDeleteView.as_view(), name='retrieve-update-delete-movies'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie-stats'),
]
