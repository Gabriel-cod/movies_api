from django.urls import path
from .views import ReviewListCreateView, ReviewRetrieveUpdateDeleteView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='create-read-reviews'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDeleteView.as_view(), name='retrieve-update-delete-reviews'),
]