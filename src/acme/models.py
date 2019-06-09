# import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length = 20)
    descricao = models.CharField(max_length = 200)
    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length = 30)
    descricao = models.CharField(max_length = 200)
    def __str__(self):
        return self.nome

class Carro(models.Model):
    modelo = models.CharField(max_length = 50)
    marca = models.ForeignKey('Marca', on_delete = models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
    ano = models.CharField(max_length = 4)
    descricao = models.CharField(max_length = 200)
    imagem = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.modelo
    def publicar(self):
        self.save()

class Pessoa(models.Model):
    CNH = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=10, default="123456")
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    rua = models.CharField(max_length=40)
    cep = models.CharField(max_length=8)
    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    publicacaoID = models.AutoField(primary_key = True)
    carro = models.ForeignKey('Carro', on_delete = models.CASCADE)
    preco = models.FloatField()
    disponivel = models.IntegerField()
    descricao = models.CharField(max_length = 200)
    def __str__(self):
        return f'{self.carro.modelo} <-> {self.preco}'

class Aluguel(models.Model):
    aluguelID = models.AutoField(primary_key = True)
    pessoa = models.ForeignKey('Pessoa', on_delete = models.CASCADE)
    publicacao = models.ForeignKey('Publicacao', on_delete = models.CASCADE)
    data_retirada = models.DateTimeField()
    data_retorno = models.DateTimeField()
    def __str__(self):
        return f'{self.pessoa.nome} <-> {self.publicacao.carro.modelo}'
