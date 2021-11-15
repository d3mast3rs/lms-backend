from django.db import models
from django.db.models.expressions import F


class User(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=45, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=500, null=False, blank=False)

    class Meta:
        ordering = ['id']

class Book(models.Model):
    isbn = models.CharField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    publisher = models.CharField(max_length=200, null=False, blank=False)
    quantity = models.IntegerField(null=False,blank=False)

    class Meta:
        ordering = ['id']

class Author(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200, null=False, blank=False)