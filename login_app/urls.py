from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'login_app'
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name = 'profile'),
#    path('', views.person_test, name='login'),
#    path('<int:pid>/', views.person_test_detail, name='person-test-id'),
#    path('form-test/', views.form_test, name='form-test'),

]
