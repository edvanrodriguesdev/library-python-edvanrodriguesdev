from django.db import models
from users.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    pages = models.CharField(max_length=50)

    def notify_followers(self):
        followers = self.followers.all()

        for follower in followers:
            subject = 'Atualização do livro'
            message = f"O livro {self.name} teve uma atualização."
            recipient_list = [follower.email]
            sender = follower.email  # Endereço de e-mail do seguidor como remetente
            send_mail(subject, message, sender, recipient_list)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Book_follow = models.ManyToManyField(Book)
