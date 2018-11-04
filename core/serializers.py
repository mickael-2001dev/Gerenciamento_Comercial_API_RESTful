from rest_framework import serializers
from .models import Marca, Carro


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nome')

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('id', 'modelo', 'ano', 'preco', 'marca')