from django.urls import path
from . import views

urlpatterns = [
    path("copy/", views.CopyViews.as_view()),
]
