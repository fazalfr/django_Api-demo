# from pyexpat import model
from django.db import models

# Create your models here.
class Users(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)


class Ebook(models.Model):
    Title=models.CharField(max_length=100)
    Auther=models.CharField(max_length=100)
    Genre=models.CharField(max_length=100)
    Rating=models.CharField(max_length=100)
    Favourite=models.BooleanField(default=True)
