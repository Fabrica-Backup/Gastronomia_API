from decimal import *

from rest_framework import serializers

from .models import Ingrediente
from unidades_medida.serializers import UnidadeMedidaSerializer

class CreateIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_caloria_ingrediente',
            'aproveitamento_ingrediente',
            'unidades_medida'
        ]

    def validate(self, data):
        nome_ingrediente = data['nome_ingrediente']
        quantidade_caloria = Decimal(data['quantidade_caloria_ingrediente'])
        aproveitamento = Decimal(data['aproveitamento_ingrediente'])
        nome_qs = Ingrediente.objects.filter(nome_ingrediente=nome_ingrediente)

        if nome_qs.exists():
            raise serializers.ValidationError('Já existe um ingrediente cadastrado com este nome')
        elif quantidade_caloria < 0:
            raise serializers.ValidationError('O campo quantidade caloria não pode ser negativo')
        elif aproveitamento < 0:
            raise serializers.ValidationError('O Campo aproveitamento não pode ser negativo')
        return data

class ListIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_caloria_ingrediente',
            'aproveitamento_ingrediente',
            'quantidade_estoque_ingrediente',
            'quantidade_reservada_ingrediente',
            'motivo_retirada_estoque',
            'unidades_medida'
        ]

class DetailsIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_caloria_ingrediente',
            'aproveitamento_ingrediente',
            'quantidade_estoque_ingrediente',
            'quantidade_reservada_ingrediente',
            'motivo_retirada_estoque',
            'unidades_medida'
        ]

    def validate(self, data):
        nome_ingrediente = data['nome_ingrediente']
        quantidade_caloria = Decimal(data['quantidade_caloria_ingrediente'])
        aproveitamento = Decimal(data['aproveitamento_ingrediente'])
        quantidade_estoque = Decimal(data['quantidade_estoque_ingrediente'])
        quantidade_reservada = Decimal(data['quantidade_reservada_ingrediente'])
        nome_qs = Ingrediente.objects.filter(nome_ingrediente=nome_ingrediente)

        if nome_qs.exists():
            raise serializers.ValidationError('Já existe um ingrediente cadastrado com este nome')
        if quantidade_caloria < 0:
            raise serializers.ValidationError('O campo quantidade caloria não pode ser negativo')
        elif aproveitamento < 0:
            raise serializers.ValidationError('O Campo aproveitamento não pode ser negativo')
        elif quantidade_estoque < 0:
            raise serializers.ValidationError('O campo quantidade em estoque não pode ser negativo')
        elif quantidade_reservada < 0:
            raise serializers.ValidationError('O Campo quantidade reservada não pode ser negativo')
        return data
