from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    categoriaID = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 20)

class Marca(models.Model):
    marcaID = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 30)
    descricao = models.CharField(max_length = 200)

class Carro(models.Model):
    carID = models.AutoField(primary_key = True)
    marca = models.ForeignKey('Marca', on_delete = models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
    modelo = models.CharField(max_length = 50)
    ano = models.DateTimeField()
    descricao = models.CharField(max_length = 200)
    def publicar(self):
        self.save()

class Pessoa(models.Model):
    pessoaID = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=50)


class Publicacao(models.Model):
    publicacaoID = models.AutoField(primary_key = True)
    carro = models.ForeignKey('Carro', on_delete = models.CASCADE)
    preco = models.FloatField()
    disponivel = models.IntegerField()
    descricao = models.CharField(max_length = 200)

class Aluguel(models.Model):
    aluguelID = models.AutoField(primary_key = True)
    pessoa = models.ForeignKey('Pessoa', on_delete = models.CASCADE)
    publicacao = models.ForeignKey('Publicacao', on_delete = models.CASCADE)
    data_retirada = models.DateTimeField()
    data_retorno = models.DateTimeField()
