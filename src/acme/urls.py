from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('cars', views.get_cars, name = 'cars'),
    path('offers', views.offers, name = 'offers'),
    path('about', views.about, name = 'about'),
    path('account', views.account, name = 'account'),
]