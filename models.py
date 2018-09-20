# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Categoria(models.Model):
	title 		= models.CharField(max_length=200, primary_key=True)

	def __str__(self):
		return self.title

class Carteira(models.Model):
	ContaChoises = (("CTCR","Conta Corrente"),
					("CARTCRED","Cartão de Crédito"),
					("DIN","Dinheiro em Especie"))
	title 			= models.CharField(max_length=200, primary_key=True)
	saldo 			= models.DecimalField("Saldo da Conta", max_digits=6, decimal_places=2)
	ult_atualizacao = models.DateTimeField("Data da Ultima atualização",default=timezone.now)
	tipo 			= models.CharField("Tipo de Conta", choices=ContaChoises, default="CTCR",max_length=20)
	banco 			= models.IntegerField("Número do Banco")
	agencia 		= models.IntegerField("Número da Agência")
	conta 			= models.IntegerField("Número da Conta")
	digito 			= models.IntegerField("Digito")
	no_cartao 		= models.CharField("Número do Cartão", max_length=50)
	limite 			= models.DecimalField("Limite da Conta", max_digits=6, decimal_places=2)

	def __str__(self):
		self.ult_atualizacao = timezone.now()
		return self.title

class lancamento(models.Model):

	EfetuadoChoises= (("Pgo", "Pago"),
                      ("Pend","Pendente"),
                      ("Canc","Cancelado"),
                      ("Adia","Adiado"))
	
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)

	lancamento = models.CharField("Descrição do Lançamento", max_length=400)
	data_vencimento = models.DateField("Data do Vencimento")
	ref_pgto_atual = models.IntegerField("Parcela Atual", default=1, null=False)
	ref_pgto_total = models.IntegerField("Total de Parcelas", default=1, null=False)
	
	des_categoria = models.ForeignKey(Categoria)
	flg_mandatorio = models.BooleanField(default=False)
	cod_barras = models.CharField("Descrição do Lançamento", max_length=400)
	nm_carteira = models.ForeignKey(Carteira)
	cpf_cnpj_cedente = models.IntegerField("CPF/CNPJ do Cedente")
    
   	data_pagamento = models.DateField("Data do Pagamento Efetuado")
	valor_pagamento = models.DecimalField("Valor do Pagamento", max_digits=6, decimal_places=2)
	efetuado = models.CharField("Status Pagamento", choices=EfetuadoChoises, default="Pend", max_length=10)

	def publish(self):
		self.save()

	def __str__(self):
		return self.lancamento