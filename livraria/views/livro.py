from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import (LivroSerializer, LivroDetailSerializer, LivroListSerializer)

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