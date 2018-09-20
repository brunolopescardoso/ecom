# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-20 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cofferBackend', '0007_auto_20180920_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='agencia',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número da Agência'),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='banco',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número do Banco'),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='conta',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número da Conta'),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='digito',
            field=models.IntegerField(blank=True, null=True, verbose_name='Digito'),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='limite',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Limite da Conta'),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='no_cartao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número do Cartão'),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='saldo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Saldo da Conta'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='cod_barras',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Descrição do Lançamento'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='cpf_cnpj_cedente',
            field=models.IntegerField(blank=True, null=True, verbose_name='CPF/CNPJ do Cedente'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Pagamento Efetuado'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='data_vencimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Vencimento'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='des_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cofferBackend.Categoria'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='nm_carteira',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cofferBackend.Carteira'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='ref_pgto_atual',
            field=models.IntegerField(blank=True, default=1, verbose_name='Parcela Atual'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='ref_pgto_total',
            field=models.IntegerField(blank=True, default=1, verbose_name='Total de Parcelas'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='#Tags'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='tipo_despesa',
            field=models.CharField(blank=True, choices=[('fixo', 'Fixo'), ('var', 'Variável')], default='var', max_length=10, null=True, verbose_name='Tipo Despesa'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='valor_pagamento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Valor Efetuado'),
        ),
    ]