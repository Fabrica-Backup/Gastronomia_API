from django.db import models

class Classificacao(models.Model):
    id_classificacao = models.AutoField(primary_key = True)
    descricacao_classificacao = models.CharField(max_length = 100)
