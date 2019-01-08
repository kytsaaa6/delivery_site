from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'login_app'
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),

#    path('', views.person_test, name='login'),
#    path('<int:pid>/', views.person_test_detail, name='person-test-id'),
#    path('form-test/', views.form_test, name='form-test'),

]
