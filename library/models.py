from django.db import models
from django.db.models.expressions import F
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=200, unique = True)
    type = models.CharField(max_length = 40)
    dob = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, null=True, blank=True) # male, female or other

    groups = None
    username = None
    last_login = None
    is_superuser = None
    is_staff = None
    date_joined = None
    user_permissions = None
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class LibraryCard(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null = True, blank=False)
    last_name = models.CharField(max_length=200, null = True, blank=False)  
    
class Book(models.Model):
    isbn = models.CharField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    publisher = models.ForeignKey('Publisher', related_name='books', blank=True, on_delete=models.PROTECT)
    num_of_available = models.IntegerField(null=False,blank=False)
    num_of_issued = models.IntegerField(default=0, null=False, blank=False)
    authors = models.ManyToManyField('Author', related_name='books', blank=True)
    users_who_issued = models.ManyToManyField('LibraryCard', related_name='books_issued', blank=True)

    class Meta:
        ordering = ['id']

class Author(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        ordering = ['id']

class Genre(models.Model):
    genre = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        ordering = ['id']

class Publisher(models.Model):
    publisher = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        ordering = ['id']