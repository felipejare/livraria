from django.contrib import admin

from livraria.models import Autor, Categoria, Editora

admin.site.register(Categoria)

admin.site.register(Editora)

admin.site.register(Autor)