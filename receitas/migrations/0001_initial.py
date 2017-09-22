# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classificacoes', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id_receita', models.AutoField(primary_key=True, serialize=False)),
                ('nome_receita', models.CharField(max_length=100)),
                ('modo_preparo_receita', models.TextField(max_length=6500)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='categorias.Categoria')),
                ('id_classificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classificacao', to='classificacoes.Classificacao')),
            ],
        ),
    ]