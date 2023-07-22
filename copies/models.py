from django.db import models
from django.utils import timezone
from django.utils import dates


class Copy(models.Model):

    is_available = models.BooleanField(default=True)
    rented = models.CharField(max_length=45, null=True)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies",
    )
