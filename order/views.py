from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Basket, Order

def basket(request):
    if request.method == 'POST':
        data = Basket.objects.all()
        form = StoreForm(request.POST, request.FILES)  # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid():
            data.save()
            return redirect('create')
    else:
        form = StoreForm()
    return render(request, 'store/store.html', {
        'form': form,
    })
# Create your views here.
