from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carro, Pessoa, Publicacao, Aluguel, Agendamento
from django.contrib import messages
from .forms import PessoaCreateForm, LoginForm, AgendamentoForm, BuscaForm
import datetime

# stripe.api_key = "pk_test_LSkKTymuMxmZ468ROAHkVpPT00b7FukC9b"
# Create your views here.
# httpresponse should be given as parameters the path to the html file of the page
def logedin(request):
    if request.session.has_key('username'):
        return True
    return False

def logout(request):
    request.session.flush()
    return redirect('login')

def checkout(request):
    if not logedin(request):
        messages.warning(request, "faça o login")
        return redirect('login')
    context={
        'logedin': logedin(request),
    }
    context['announce'] = Publicacao.objects.get(publicacaoID=request.GET['announce'])
    alugueis = Aluguel.objects.filter(publicacao=Publicacao.objects.get(publicacaoID=request.GET['announce']))
    datas=[]
    for aluguel in alugueis:
        r=[aluguel.data_retirada-datetime.timedelta(days=x) for x in range(0, (aluguel.data_retorno-aluguel.data_retirada).days)]
        datas+=r
    context['datas'] = datas
    return render(request, 'acme/checkout.html', context)

def index(request):
    if request.method == 'POST':
        if not logedin(request):
            messages.warning(request, "faça o login")
            return redirect('login')
        form = AgendamentoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            Agendamento.objects.create(
                pessoa = Pessoa.objects.get(nome=request.session['username']),
                data_retirada = form.cleaned_data.get('data_retirada'),
                data_retorno = form.cleaned_data.get('data_retorno'),
                cidade = form.cleaned_data.get('cidade'),
                estado = form.cleaned_data.get('estado'),
            )
            messages.success(request, "Solicitação de agendamento feita com sucesso, entraremos em contato")
    context={
        'logedin': logedin(request),
    }
    return render(request, 'acme/index.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data.get('user_nome')
            s = form.cleaned_data.get('user_senha')
            query = f"SELECT * FROM acme_pessoa WHERE nome='{n}' AND senha='{s}'"
            if Pessoa.objects.raw(query):
                request.session['username'] = n
                messages.success(request, f'Login com sucesso, User: {n}')
                return redirect('index')
        messages.warning(request, "usuário ou senha inválidos")
    return render(request, 'acme/login.html')

def signup(request):
    context={
        'logedin': logedin(request),
    }
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
        context['form'] = PessoaCreateForm()
    return render(request, 'acme/signup.html', context)

def cars(request):
    if request.method == 'POST':
        if not logedin(request):
            messages.warning(request, "faça o login")
            return redirect('login')
        form = AgendamentoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            Agendamento.objects.create(
                pessoa = Pessoa.objects.get(nome=request.session['username']),
                data_retirada = form.cleaned_data.get('data_retirada'),
                data_retorno = form.cleaned_data.get('data_retorno'),
                cidade = form.cleaned_data.get('cidade'),
                estado = form.cleaned_data.get('estado'),
            )
            messages.success(request, "Solicitação de agendamento feita com sucesso, entraremos em contato")
    context={
        'logedin': logedin(request),
    }
    context['carros'] = Carro.objects.all()
    return render(request, 'acme/carros.html', context)

def account(request):
    if not logedin(request):
        messages.warning(request, "faça o login")
        return redirect('login')
    context={
        'logedin': logedin(request),
    }
    query = f"SELECT * FROM acme_pessoa WHERE nome='{request.session.get('username')}'"
    Pessoa.objects.raw()
    return render(request, 'acme/account.html', context)

def offers(request):
    context={
        'logedin': logedin(request),
    }
    ofertas = Publicacao.objects.all()
    if request.method == 'POST':
        form = BuscaForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data.get('perkm'))
            ofertas.filter(perkm=form.cleaned_data.get('perkm'))
            if form.cleaned_data.get('minpreco'):
                ofertas = ofertas.filter(preco__gte=form.cleaned_data.get('minpreco'))
            if form.cleaned_data.get('maxpreco'):
                ofertas = ofertas.filter(preco__lte=form.cleaned_data.get('maxpreco'))
            if form.cleaned_data.get('modelo'):
                ofertas = ofertas.filter(carro__modelo__contains=form.cleaned_data.get('modelo'))
            if form.cleaned_data.get('marca'):
                ofertas = ofertas.filter(carro__marca__nome__contains=form.cleaned_data.get('marca'))
    context['offers'] = ofertas
    return render(request, 'acme/offers.html', context)

def about(request):
    context={
        'logedin': logedin(request),
    }
    return render(request, 'acme/about.html', context)