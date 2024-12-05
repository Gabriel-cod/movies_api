from django.urls import path
from .views import ActorListCreateView, ActorRetrieveUpdateDeleteView

urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name='create-read-actors'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDeleteView.as_view(), name='retrieve-update-delete-actors'),
]