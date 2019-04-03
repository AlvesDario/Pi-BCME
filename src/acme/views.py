from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carro
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
# httpresponse should be given as parameters the path to the html file of the page

def index(request):
    return render(request, 'acme/index.html')

def login(request):
    return render(request, 'acme/login.html', {'css': 'acme/login.css'})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for user {username}')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'acme/signup.html', { 'form': form })

def cars(request):
    return HttpResponse('cars')

def offers(request):
    return HttpResponse('offers')

def about(request):
    return HttpResponse('about')

def account(request):
    return HttpResponse('account')

def get_cars(request):
    carros = Carro.objects.all()
    return render(request, 'acme/carros.html', {'cars': carros})
