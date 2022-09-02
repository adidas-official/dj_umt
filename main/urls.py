from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='register'),
    path('login/', views.login_adv, name='login'),
]