from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "is_available", "rented", "book_id"]
        extra_kwargs = {"id": {"read_only": True}, "rented": {"write_only": True}}

    def create(self, data):
        return Copy.objects.create(**data)
