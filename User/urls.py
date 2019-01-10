#    path('', views.login, name = 'login'),
#    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#    path('profile/', views.profile, name = 'profile'),
#    path('', views.person_test, name='login'),
#    path('<int:pid>/', views.person_test_detail, name='person-test-id'),
#    path('form-test/', views.form_test, name='form-test'),



from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
#    path('profile/', views.profile, name = 'profile'),
    path('join/', views.join, name = 'join'),
    path('success/',views.success, name = 'success'),
]