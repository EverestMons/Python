from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User (models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quote (models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    users = models.ForeignKey(User, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
