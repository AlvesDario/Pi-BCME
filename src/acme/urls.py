from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('signup/', views.signup, name = 'signup'),
    # path('login/', views.login, name = 'login'),
    path('login/', auth_views.LoginView.as_view(template_name = 'acme/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'acme/logout.html'), name = 'logout'),
    path('cars/', views.get_cars, name = 'cars'),
    path('offers/', views.offers, name = 'offers'),
    path('about/', views.about, name = 'about'),
    path('account/', views.account, name = 'account'),
]