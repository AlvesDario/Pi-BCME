from django import forms

class LoginForm(forms.Form):
    user_nome = forms.CharField(label='Nome do Usuário', max_length=20)
    user_senha = forms.CharField(label='Senha do Usuário', max_length=6)

class PessoaCreateForm(forms.Form):
    CNH = forms.CharField(label='CNH ',max_length=11)
    nome = forms.CharField(label='Nome ',max_length=50)
    senha = forms.CharField(label='Senha ',max_length=10)
    email = forms.CharField(label='email ',max_length=50)
    telefone = forms.CharField(label='Telefone ',max_length=11)
    endereco = forms.CharField(label='Endereco ',max_length=50)
    rua = forms.CharField(label='Rua ',max_length=40)
    cep = forms.CharField(label='CEP ',max_length=8)