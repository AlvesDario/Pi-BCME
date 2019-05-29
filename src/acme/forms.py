from django import forms

class LoginForm(forms.Form):
    user_nome = forms.CharField(label='Nome do Aluno', max_length=20)
    user_senha = forms.CharField(label='Senha do Aluno', max_length=6)