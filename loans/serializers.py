from rest_framework import serializers
from .models import Loan
from copies.models import Copy
from users.models import User
from django.utils import timezone
from datetime import datetime, timedelta


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "id",
            "copy_id",
            "user_id",
            "created_date",
            "end_date",
            "book_returned"
        ]
        read_only_fields = ["id", "created_date", "end_date", "book_returned"]

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = User.objects.get(id=validated_data["user_id"])
        if user["is_block"]:
            updated_date = timezone.now()
            blocked_date = updated_date + timedelta(hours=72)
            user.is_block = blocked_date
            user.save()
