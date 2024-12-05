from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDeleteView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='create-read-movies'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDeleteView.as_view(), name='retrieve-update-delete-movies'),
]