from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from project.permissions import GlobalPermissionClass
from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Movie.objects.all()

    def get(self, request):
        return response.Response(
            data={"message": "Here are the stats."},
            status=status.HTTP_200_OK
        )
