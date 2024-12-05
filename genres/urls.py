from django.urls import path
from .views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='create-read-genres'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete-genres'),

]