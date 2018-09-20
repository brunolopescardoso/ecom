from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
	
class Usuario(models.Model):
	#Identificação
	idusuario	= models.CharField("Email", max_length=200, primary_key=True)
	pri_nome	= models.CharField("Nome", max_length=100, null=True, blank=True)
	ult_nome	= models.CharField("Sobrenome", max_length=200, null=True, blank=True)
	
	#Dados Pessoais
	cpf			= models.CharField("CPF (opcional)", unique=True, max_length=15,  blank=True, null=True)
	dt_nasc		= models.DateField("Data Nascimento", null=True, blank=True)
	
	#Controle
	idFirebase  = models.CharField(max_length=200, blank=True, null=True)
	dt_cadastro = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.idusuario
		
		
class Carteira(models.Model):
	usuario		= models.ForeignKey(Usuario)

	ContaChoises = (("CTCR","Conta Corrente"),
					("CARTCRED","Cartão de Crédito"),
					("DIN","Dinheiro em Especie"),
					("POU","Poupança"),
					("OUT","Outros"))
					
	#Identificação
	carteira		= models.CharField(max_length=200, primary_key=True)
	saldo 			= models.DecimalField("Saldo da Conta", max_digits=6, decimal_places=2, null=True, blank=True)
	ult_atualizacao = models.DateTimeField("Data da Ultima atualização",auto_now_add=True)
	
	#Dados Adicionais
	tipo 			= models.CharField("Tipo de Conta", choices=ContaChoises, default="CTCR",max_length=20)
	banco 			= models.IntegerField("Número do Banco", null=True, blank=True)
	agencia 		= models.IntegerField("Número da Agência", null=True, blank=True)
	conta 			= models.IntegerField("Número da Conta", null=True, blank=True)
	digito 			= models.IntegerField("Digito", null=True, blank=True)
	no_cartao 		= models.CharField("Número do Cartão", max_length=50, null=True, blank=True)
	limite 			= models.DecimalField("Limite da Conta", max_digits=6, decimal_places=2, null=True, blank=True)

	def __str__(self):
		self.ult_atualizacao = timezone.now()
		return self.carteira

		
class Categoria(models.Model):
	categoria		= models.CharField(max_length=200, primary_key=True)

	def __str__(self):
		return self.categoria

		
class Lancamento(models.Model):
	#Opções
	EfetuadoChoises	= (("Pgo", "Pago"),
                      ("Pend","Pendente"),
                      ("Canc","Cancelado"),
                      ("Adia","Adiado"))
					  
	tipoChoises		= (("fixo", "Fixo"),
                      ("var","Variável"))
	
	#Identificação do usuário
	author 			= models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nm_carteira 	= models.ForeignKey(Carteira, null=True, blank=True)
	created_date 	= models.DateTimeField(auto_now_add=True)

	#id lançamento (O QUE)
	lancamento 		= models.CharField("Descrição do Lançamento", max_length=400, primary_key=True)
	valor			= models.DecimalField("Valor", max_digits=6, decimal_places=2, null=True, blank=True)
	
	#Dados do lancçamento (QUANDO)
	data_vencimento = models.DateField("Data do Vencimento", null=True, blank=True)
	ref_pgto_atual	= models.IntegerField("Parcela Atual", default=1, null=False, blank=True)
	ref_pgto_total 	= models.IntegerField("Total de Parcelas", default=1, null=False, blank=True)
	flg_mandatorio 	= models.BooleanField("Pagamento Obrigatório", default=False)
	
	#Dados Cedente	(PRA QUEM)
	cod_barras 		= models.CharField("Descrição do Lançamento", max_length=400, null=True, blank=True)
	cpf_cnpj_cedente = models.IntegerField("CPF/CNPJ do Cedente", null=True, blank=True)
	
	#Dados do Pagamento
	data_pagamento 	= models.DateField("Data do Pagamento Efetuado", null=True, blank=True)
	valor_pagamento = models.DecimalField("Valor Efetuado", max_digits=6, decimal_places=2, null=True, blank=True)
	efetuado 		= models.CharField("Status Pagamento", choices=EfetuadoChoises, default="Pend", max_length=10)
	
	#Categorização
	des_categoria 	= models.ForeignKey(Categoria, null=True, blank=True)
	tags			= models.CharField("#Tags", max_length=500, null=True, blank=True)
	tipo_despesa 	= models.CharField("Tipo Despesa", choices=tipoChoises, default="var", max_length=10, null=True, blank=True)
	
	
	def publish(self):
		self.save()

	def __str__(self):
		return self.lancamento