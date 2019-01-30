from django.db import models

class Basket(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)


class Order(models.Model):
    pass
# Create your models here.
