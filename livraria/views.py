from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Autor, Livro
from livraria.serializers import (
    CategoriaSerializer,
    EditoraSerializer,
    AutorSerializer,
    LivroSerializer,
    LivroDetailSerializer,
    
)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
