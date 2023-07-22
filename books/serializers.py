from django.db import models
from rest_framework import serializers
from .models import Book, Profile
from django.shortcuts import render, redirect
# from users.serializer import UsersSerializer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "name", "author", "description", "pages"]
