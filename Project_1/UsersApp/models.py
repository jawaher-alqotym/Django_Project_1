from django.db import models
from django import forms


class User(models.Model):
    user_name = models.CharField(unique=True ,max_length = 25)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length = 25)

    def __str__(self):
        return f'{self.user_name} {self.first_name} {self.last_name}'


