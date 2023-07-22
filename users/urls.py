from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
]
