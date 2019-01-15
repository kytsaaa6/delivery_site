from django.urls import path
from . import views


urlpatterns = [
    path('', views.storeList, name='list'),
    path('int:store_id>/', views.storeDetail, name='detail'),
#    path('order/', include('store_app.urls')),
#    path('login/', include('login_app.urls')),
]
