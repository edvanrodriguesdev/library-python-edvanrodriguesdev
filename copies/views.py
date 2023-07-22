from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Copy
from .serializers import CopySerializer
from books.models import Book
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class CopyViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        id = self.request.data["book_id"]
        get_book = get_object_or_404(Book, id=id)
        serializer.save(book=get_book)
    
    @extend_schema(
        operation_id = 'Copy_get', #(1)
        parameters=[CopySerializer],
        request=CopySerializer, #(3)
        responses={200:CopySerializer}, #(4)
        description = 'Rota para ver as Cópias', #(5)
        summary = 'Ver cópias', #(6)
        tags = ['Copy'], #(8)
        )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id = 'Copy_post', #(1)
        parameters=[CopySerializer],
        request=CopySerializer, #(3)
        responses={200:CopySerializer}, #(4)
        description = 'Rota para criar as Cópias', #(5)
        summary = 'Criar cópias', #(6)
        tags = ['Copy'], #(8)
        )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)