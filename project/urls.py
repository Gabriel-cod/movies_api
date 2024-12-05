from django.contrib import admin
from django.urls import path
from genres import views as genre_views
from actors import views as actor_views
from movies import views as movie_views
from reviews import views as reviews_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', genre_views.GenreListCreateView.as_view(), name='create-read-genres'),
    path('genres/<int:pk>/', genre_views.GenreRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete-genres'),
    
    path('actors/', actor_views.ActorListCreateView.as_view(), name='create-read-actors'),
    path('actors/<int:pk>/', actor_views.ActorRetrieveUpdateDeleteView.as_view(), name='retrieve-update-delete-actors'),
    
    path('movies/', movie_views.MovieListCreateView.as_view(), name='create-read-movies'),
    path('movies/<int:pk>/', movie_views.MovieRetrieveUpdateDeleteView.as_view(), name='retrieve-update-delete-movies'),
    
    path('reviews/', reviews_views.ReviewListCreateView.as_view(), name='create-read-reviews'),
    path('reviews/<int:pk>/', reviews_views.ReviewRetrieveUpdateDeleteView.as_view(), name='retrieve-update-delete-reviews'),
]
