# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classificacoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classificacao',
            old_name='descricacao_classificacao',
            new_name='descricao_classificacao',
        ),
    ]
