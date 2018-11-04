from django.shortcuts import render
from rest_framework import viewsets
from .models import Marca, Carro
from .serializers import MarcaSerializer, CarroSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer