from django.db import models

from unidades_medida.models import UnidadeMedida

class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key = True)
    nome_ingrediente = models.CharField(max_length = 200)
    quantidade_caloria_ingrediente = models.DecimalField(max_digits = 6, decimal_places = 1)
    aproveitamento_ingrediente = models.DecimalField(max_digits = 4, decimal_places = 1)
    quantidade_estoque_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2 , null = True)
    quantidade_reservada_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2 , null = True)
    motivo_retirada_estoque = models.CharField(max_length = 200 , null = True)
    unidades_medida = models.ForeignKey(UnidadeMedida, related_name = 'unidades_medida', on_delete = models.CASCADE)
