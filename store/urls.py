from django.urls import path
from . import views

urlpatterns = [
    path('', views.storeList, name = 'list'),
    path('<int:store_id>/', views.storeDetail, name = 'detail'),
    path('<int:store_id>/<str:menu>/', views.storeMenu, name = 'storemenu'),
    path('create/', views.storeCreate, name = 'create'),
#    path('update/', views.storeUpdate, name = 'update'),
    path('<pk>/delete/', views.storeDelete, name = 'delete'),
#    path('login/', include('login_app.urls')),
]