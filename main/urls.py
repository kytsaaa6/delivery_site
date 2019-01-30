from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
#    path('login/', include('login_app.urls')),
]