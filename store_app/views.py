from django.shortcuts import render
from django.http import HttpResponse
from .models import Store


def storeList(request):
    data = Store.objects.first()

    return render(request, "test.html", context=data)

def storeDetail(request):
    detail = Store.objects.all
# Create your views here.
