from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Basket
from store.models import Menu

def basket(request):
    menu = Menu.objects.get(store=request.POST.get('store'), name=request.POST.get('menu'))
    data = Basket()
    store = menu.store
    data.menu = menu
    data.name = request.POST.get('name')
    data.price = request.POST.get('price')
    data.count = request.POST.get('count')
    data.total = int(data.count) * int(data.price)
    data.save()

    context = {
        'data':data,
        'store':store
    }

    return render(request, 'order/basket.html', context)

def order(request):
    pass
# Create your views here.
