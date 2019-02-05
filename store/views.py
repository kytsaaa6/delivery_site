from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from .models import Store, Menu
from .forms import StoreForm, MenuForm


def storeList(request):
    if request.method == 'GET':
        data = Store.objects.all()
    return render(request, 'store/index.html', {'data':data})

def storeDetail(request, store_id):
    if request.method == 'GET':
        store = Store.objects.get(id=store_id)
        menuz = store.menu_set.all

        context = {
            'store' : store,
            'menuz' : menuz
        }
    return render(request, 'store/detail.html', context)

def storeMenu(request, store_id, menu):
    if request.method == 'GET':
        store = Store.objects.get(id=store_id)
        data = Menu.objects.filter(store=store, name=menu)

        context = {
            'data' : data,
            'store' : store
        }

    return render(request, 'store/menu.html', context)

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
