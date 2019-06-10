from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carro, Pessoa
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import PessoaCreateForm, LoginForm
# import stripe

# stripe.api_key = "pk_test_LSkKTymuMxmZ468ROAHkVpPT00b7FukC9b"
# Create your views here.
# httpresponse should be given as parameters the path to the html file of the page
def logedin(request):
    if request.session.has_hey('user'):
        return True
    return False

def logout(request):
    request.session.flush()
    return redirect('login')

def checkout(request):
    if logedin(request):
        messages.warning(request, "faça o login")
        return redirect('login')
    return render(request, 'acme/checkout.html')

def index(request):
    return render(request, 'acme/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data.get('user_nome')
            s = form.cleaned_data.get('user_senha')
            query = f"SELECT * FROM acme_pessoa WHERE nome='{n}' AND senha='{s}'"
            if Pessoa.objects.raw(query):
                request.session['username'] = n
                messages.success(request, f'Login com sucesso, User: {pessoa.nome}')
                return redirect('index')
        messages.warning(request, "usuário ou senha inválidos")
    return render(request, 'acme/login.html')#, {'css': 'acme/login.css'})

def signup(request):
    if request.method == 'POST':
        form = PessoaCreateForm(request.POST)
        if form.is_valid():
            Pessoa.objects.create(
                CNH = form.cleaned_data.get('CNH'),
                nome = form.cleaned_data.get('nome'),
                senha = form.cleaned_data.get('senha'),
                email = form.cleaned_data.get('email'),
                telefone = form.cleaned_data.get('telefone'),
                endereco = form.cleaned_data.get('endereco'),
                rua = form.cleaned_data.get('rua'),
                cep = form.cleaned_data.get('cep')
            )
            username = form.cleaned_data.get('nome')
            messages.success(request, f'Account created for user {username}')
            return redirect('login')
    else:
        form = PessoaCreateForm()
    return render(request, 'acme/signup.html', { 'form': form })

def cars(request):
    carros = Carro.objects.all()
    return render(request, 'acme/carros.html', {'cars': carros})

def offers(request):
    return render(request, 'acme/offers.html')

def about(request):
    return HttpResponse('about')

def account(request):
    return HttpResponse('account')