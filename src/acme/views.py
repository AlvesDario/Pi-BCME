from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# httpresponse should be given as parameters the path to the html file of the page

def index(request):
    return HttpResponse('home page')

def login(request):
    return HttpResponse('login')

def signin(request):
    return HttpResponse('signin')

def cars(request):
    return HttpResponse('cars')

def offers(request):
    return HttpResponse('offers')

def about(request):
    return HttpResponse('about')

def account(request):
    return HttpResponse('account')

# def (request):
