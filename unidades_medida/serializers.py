from rest_framework import serializers
from .models import UnidadeMedida

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = [
            'id_unidade_medida',
            'simbolo_unidade_medida',
            'descricao_unidade_medida'
        ]
