from django.urls import path
from . import views

urlpatterns = [
   path("loan/", views.LoanView.as_view()),
   path("loan/<int:pk>/", views.LoanDetailView.as_view())
]
