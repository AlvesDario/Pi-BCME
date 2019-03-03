from django.contrib import admin
from .models import Marca, Carro, Pessoa, Publicacao, Aluguel

admin.site.register(Marca)
admin.site.register(Carro)
admin.site.register(Pessoa)
admin.site.register(Publicacao)
admin.site.register(Aluguel)