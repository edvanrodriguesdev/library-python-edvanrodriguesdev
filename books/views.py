from django.shortcuts import render
from .models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from users.permissions import IsUserOrAdmin
from drf_spectacular.utils import extend_schema


class BookView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @extend_schema(
        operation_id="Books_get",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={200: BookSerializer},  # (4)
        description="Rota para ver os Livros",  # (5)
        summary="Ver Livros",  # (6)
        tags=["Books"],  # (8)
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CreateBookView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOrAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @extend_schema(
        operation_id="Books_id_post",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={201: BookSerializer},  # (4)
        description="Rota para criar Livros",  # (5)
        summary="Criar Livros",  # (6)
        tags=["Books"],  # (8)
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOrAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"

    @extend_schema(
        operation_id="Books_id_get",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={200: BookSerializer},  # (4)
        description="Rota para ver um Livro específico",  # (5)
        summary="Ver um Livro",  # (6)
        tags=["Books"],  # (8)
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Books_id_delete",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={204: "No content"},  # (4)
        description="Rota para deletar um Livro específico",  # (5)
        summary="Deletar um Livro",  # (6)
        tags=["Books"],  # (8)
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(operation_id="Books_id_put", exclude=True)  # (1)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="Books_id_patch",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={202: BookSerializer},  # (4)
        description="Rota para alterar um Livro específico",  # (5)
        summary="Alterar um Livro",  # (6)
        tags=["Books"],  # (8)
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class CustomBookDetailView(BookDetailView):
    def perform_update(self, serializer):
        book = self.get_object()
        serializer.save()
        book.notify_followers()
        # criada para fazer o chamado da notify_followers()


class FollowBookView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    @extend_schema(
        operation_id="Books_id_follow_patch",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={200: BookSerializer},  # (4)
        description="Rota para alterar o follow de um Livro específico",  # (5)
        summary="Altera o follow de um Livro",  # (6)
        tags=["Follow"],  # (8)
    )
    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        request.user.followed_books.add(book)
        serializer = BookSerializer(book)
        book_return = {book.name, "Livro seguido com sucesso"}
        return Response(book_return)

    @extend_schema(
        operation_id="Books_id_follow_get",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={200: BookSerializer},  # (4)
        description="Rota para ver o follow de um Livro específico",  # (5)
        summary="Ver o follow de um Livro",  # (6)
        tags=["Follow"],  # (8)
    )
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        request.user.followed_books.add(book)
        return Response(book)


class UnfollowBookView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    @extend_schema(
        operation_id="Books_id_follow_delete",  # (1)
        parameters=[BookSerializer],
        request=BookSerializer,  # (3)
        responses={200: BookSerializer},  # (4)
        description="Rota para deletar o follow de um Livro específico",  # (5)
        summary="Deleta o follow de um Livro",  # (6)
        tags=["Follow"],  # (8)
    )
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        request.user.followed_books.remove(book)
        book_return = {book.name, "Deixou de seguir o Livro com sucesso"}
        return Response(book_return)
