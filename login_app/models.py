from django import forms
from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    birth = models.DateTimeField('date published')
    age = models.IntegerField()