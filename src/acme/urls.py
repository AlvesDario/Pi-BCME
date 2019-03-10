from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signin', views.signin, name = 'signin'),
    path('login', views.login, name = 'login'),
    path('cars', views.cars, name = 'cars'),
    path('offers', views.offers, name = 'offers'),
    path('about', views.about, name = 'about'),
    path('account', views.account, name = 'account'),
]