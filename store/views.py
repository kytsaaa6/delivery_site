from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Store, Menu
from .forms import StoreForm


def storeList(request):
    if request.method == 'GET':
        data = Store.objects.all()
    return render(request, 'store/index.html', {'data':data})

def storeDetail(request, store_id):
    if request.method == 'GET':
        data = Menu.objects.all()
        store = Store.objects.get(id=store_id)
    return render(request, 'store/detail.html', {'data': data, 'store':store})

def storeMenu(request, store_id, menu):
    if request.method == 'GET':
        data = Menu.objects.all()

    return render(request, 'store/menu.html', {'data': data})

def storeCreate(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)  # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid():
            store = form.save(commit=False)  # 중복 DB save를 방지
            store.save()
            return redirect('create')
    else:
        form = StoreForm()
    return render(request, 'store/store.html', {
        'form': form,
    })


def storeDelete(request, pk):
        store = Store.objects.get(pk=pk)

        if request.method == 'POST':
#            if request.POST['password'] == article.password:
            store.delete()
            return redirect('/')  # 첫페이지로 이동하기

        return render(request, 'store_remove.html', {'store': store})
# Create your views here.
