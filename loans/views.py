from rest_framework import generics
from loans.models import Loan
from rest_framework_simplejwt.authentication import JWTAuthentication
from loans.serializers import LoanSerializer
from users.models import User
from rest_framework.exceptions import ValidationError
from copies.models import Copy
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()


    def perform_create(self, serializer):
        copy_id = self.request.data.get("copy_id")
        copy = Copy.objects.get(id=copy_id)
        user_id = self.request.data.get("user_id")
        user = User.objects.get(id=user_id)

        if not copy.is_available:
            raise ValidationError("This book is not available.")

        if user.is_block:
            raise ValidationError(
                "This user is currently blocked, wait 72 hours.")

        copy.is_available = False
        copy.save()
        end_date = self.returned_rule()
        loan = serializer.save(copy=copy, user=user, end_date=end_date)
        copy.loan = loan.id
        copy.save()

    def returned_rule(self):
        updated_date = timezone.now()
        returned_date = updated_date + timedelta(days=5)
        
        if returned_date.weekday() == 5:
            returned_date += timedelta(days=2)
        if returned_date.weekday() == 6:
            returned_date += timedelta(days=1)
        return returned_date



    def get_queryset(self):
        if self.request.user.is_superuser:
            return Loan.objects.all()
        return Loan.objects.filter(user=self.request.user)
    
    @extend_schema(
        operation_id = 'Loan_get', #(1)
        parameters=[LoanSerializer],
        request=LoanSerializer, #(3)
        responses={200: LoanSerializer}, #(4)
        description = 'Rota para ver histórico de empréstimos', #(5)
        summary = 'Ver histórico',
        tags = ['Loan'], #(8)
    )   
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id = 'Loan_post', #(1)
        parameters=[LoanSerializer],
        request=LoanSerializer, #(3)
        responses={201: LoanSerializer}, #(4)
        description = 'Rota para criar o empréstimo de um Livro', #(5)
        summary = 'Criar empréstimo',
        tags = ['Loan'], #(8)
    )   
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class LoanDetailView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_update(self, serializer):
        loan = get_object_or_404(Loan, pk=self.kwargs["pk"])
        loan.book_returned = True
        loan.save()
        copy = get_object_or_404(Copy, pk=loan.copy_id)
        copy.is_available = True
        copy.save()

    @extend_schema(
        operation_id = 'Loan_id_patch', #(1)
        parameters=[LoanSerializer],
        request=LoanSerializer, #(3)
        responses={200: LoanSerializer}, #(4)
        description = 'Rota para atualizar o empréstimo de um Livro', #(5)
        summary = 'Atualizar empréstimo',
        tags = ['Loan'], #(8)
    )   
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id = 'Loan_id_put', #(1)
        exclude=True,
        deprecated=True,
        tags = ['Loan'], #(8)
    )   
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)