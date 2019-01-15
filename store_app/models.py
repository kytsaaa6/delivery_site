from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField()
    menu = models.CharField(max_length=200)


    def __str__(self):
        return self.name