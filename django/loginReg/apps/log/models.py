from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from django.contrib import messages
import bcrypt
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def login(self, email, password):
        try:
            # user = User.objects.get(email = email)
            if bcrypt.hashpw(password.encode('UTF-8'), user.password.encode('UTF-8')) == user.password:
                return user
        except:
            pass
        return None
    def registername(self, name):
        if not name.isalpha():
            return False
        if len(name) < 2:
            return False
        else:
            return name
    def registeremail(self, email):
        if not email_regex.match(email):
            return False
        else:
            return email
    def registerpassword(self, password, password2):
        if len(password) < 7:
            return False
        if not password == password2:
            return False
        else:
            return password
class User(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = UserManager()
