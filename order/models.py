from django.db import models
from store.models import Menu
from account.models import Account

class Basket(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    total = models.IntegerField(default=0)


"""
class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=)
"""
