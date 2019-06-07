from django.contrib import admin
from .models import Categoria, Marca, Carro, Pessoa, Publicacao, Aluguel
from django.contrib.auth.models import User, Group

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Carro)
admin.site.register(Pessoa)
admin.site.register(Publicacao)
admin.site.register(Aluguel)
admin.site.unregister(Group)
admin.site.unregister(User)