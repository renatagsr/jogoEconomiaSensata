from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=64)
