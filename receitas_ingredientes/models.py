from django.db import models

from receitas.models import Receita
from unidades_medidas.models import UnidadeMedida
from ingredientes.models import Ingrediente


class ReceitaIngrediente(models.Model):
    id_receita_ingrediente = models.AutoField(primary_key = True)
    id_receita = models.ForeignKey(Receita, related_name = 'id_receita', on_delete = models.CASCADE)
    id_unidade_medida = models.ForeignKey(UnidadeMedida, related_name = 'id_unidade_medida', on_delete = models.CASCADE)
    id_ingrediente =  models.ForeignKey(Ingrediente, related_name = 'id_ingrediente', on_delete = models.CASCADE)
    quantidade_bruta_receita_ingrediente = models.DecimalField(max_digits = 7, decimal_places = 2 , null = True)
    custo_bruto_receita_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2 , null = True)
