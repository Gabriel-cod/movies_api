from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project.permissions import GlobalPermissionClass
from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
