from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project.permissions import GlobalPermissionClass
from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer