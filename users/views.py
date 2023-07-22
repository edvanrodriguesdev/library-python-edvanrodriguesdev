from rest_framework import generics
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsUserOrAdmin
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema


class LoginView(TokenObtainPairView):
    ...


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(
        operation_id="Users_get",  # (1)
        parameters=[UserSerializer],
        request=UserSerializer,  # (3)
        responses={200: UserSerializer},  # (4)
        description="Rota para ver os Usuários",  # (5)
        summary="Ver Usuários",  # (6)
        tags=["Users"],  # (8)
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Users_post",  # (1)
        parameters=[UserSerializer],
        request=UserSerializer,  # (3)
        responses={201: UserSerializer},  # (4)
        description="Rota para Criar os Usuários",  # (5)
        summary="Criar Usuários",  # (6)
        tags=["Users"],  # (8)
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOrAdmin]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(
        operation_id="Users_id_get",  # (1)
        parameters=[UserSerializer],
        request=UserSerializer,  # (3)
        responses={200: UserSerializer},  # (4)
        description="Rota para ver um Usuário específico",  # (5)
        summary="Ver um Usuário",  # (6)
        tags=["Users"],  # (8)
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Users_id_patch",  # (1)
        parameters=[UserSerializer],
        request=UserSerializer,  # (3)
        responses={200: UserSerializer},  # (4)
        description="Rota para alterar um Usuário específico",  # (5)
        summary="Alterar um Usuário",  # (6)
        tags=["Users"],  # (8)
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="Users_id_delete",  # (1)
        parameters=[UserSerializer],
        request=UserSerializer,  # (3)
        responses={200: UserSerializer},  # (4)
        description="Rota para deletar um Usuário específico",  # (5)
        summary="Deleta um Usuário",  # (6)
        tags=["Users"],  # (8)
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(operation_id="Users_id_put", exclude=True, deprecated=True)  # (1)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
