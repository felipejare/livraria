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
    LivroListSerializer,
    
)

# from rest_framework.permissions import IsAuthenticated


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # permission_classes = [IsAuthenticated]


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return LivroListSerializer
    #     elif self.action == "retrieve":
    #         return LivroDetailSerializer
    #     return LivroSerializer
    
    serializer_classes = {
        "list": LivroListSerializer,
        "retrieve": LivroDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LivroSerializer)

