from rest_framework import serializers

from .models import ReceitaIngrediente
from receitas.serializers import ReceitaSerializer
from unidades_medidas.serializers import UnidadeMedidaSerializer
from ingredientes.serializers import IngredienteSerializer


class ReceitaIngredienteSerializer(serializers.ModelSerializer):
    id_receita = ReceitaSerializer()
    id_unidade_medida = UnidadeMedidaSerializer()
    id_ingrediente = IngredienteSerializer()
    class Meta:
        model = ReceitaIngrediente
        fields = [
            'id_receita_ingrediente',
            'id_receita',
            'id_unidade_medida',
            'id_ingrediente',
            'quantidade_bruta_receita_ingrediente',
            'custo_bruto_receita_ingrediente'
        ]
