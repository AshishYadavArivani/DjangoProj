from django.db import models

# Create your models here.
class login(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=255)
