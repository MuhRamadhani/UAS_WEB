from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



class Movie(models.Model):
    title = models.CharField(max_length=100)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie)
