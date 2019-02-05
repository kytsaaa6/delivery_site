from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    text = models.TextField()
    img = models.ImageField(blank=True)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name
# Create your models here.
