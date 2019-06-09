from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('cars/', views.cars, name = 'carros'),
    path('offers/', views.offers, name = 'offers'),
    path('about/', views.about, name = 'about'),
    path('account/', views.account, name = 'account'),
]

