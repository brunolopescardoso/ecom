# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-20 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cofferBackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('carteira', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Saldo da Conta')),
                ('ult_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Ultima atualização')),
                ('tipo', models.CharField(choices=[('CTCR', 'Conta Corrente'), ('CARTCRED', 'Cartão de Crédito'), ('DIN', 'Dinheiro em Especie')], default='CTCR', max_length=20, verbose_name='Tipo de Conta')),
                ('banco', models.IntegerField(null=True, verbose_name='Número do Banco')),
                ('agencia', models.IntegerField(null=True, verbose_name='Número da Agência')),
                ('conta', models.IntegerField(null=True, verbose_name='Número da Conta')),
                ('digito', models.IntegerField(null=True, verbose_name='Digito')),
                ('no_cartao', models.CharField(max_length=50, null=True, verbose_name='Número do Cartão')),
                ('limite', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Limite da Conta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cofferBackend.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]
