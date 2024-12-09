from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='obtain_pair_view'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='refresh_view'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='verify_view'),
]