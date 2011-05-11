#coding=utf8

from django.db import models

class Segmento(models.Model):
    # valores típicos: educação, saúde, governo, etc.
    nome_segmento = models.CharField(verbose_name='nome do segmento', max_length=30)

TIPO_RETENCAO_IMPOSTOS = (
    ('S', 'Sempre'), 
    ('N', 'Nunca'), 
    ('E', 'Retém em NFs Estaduais'), 
    ('M', 'Retém em NFs Municipais')
    )

class Empresa(models.Model):
    empresa = models.CharField(verbose_name='nome da empresa', max_length=30, blank=False, unique=True, db_index=True)
    porte = models.CharField(verbose_name='porte', max_length=15, choices=(('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')), blank=True, default='')
    razao_social = models.CharField(verbose_name='razão social', max_length=60, blank=False, unique=True, db_index=True)
    segmento = models.ForeignKey('Segmento', null=True) 
    atividade = models.CharField(verbose_name='atividade', max_length=60, blank=True, default='')
    data_captacao = models.DateField(verbose_name='data de captação')
    # os campos a seguir pode ter os valores: N (não), S (sim), M (somente NF municipal), E (somente NF estadual)
    retem_iss = models.CharField(verbose_name='retém ISS', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_pis = models.CharField(verbose_name='retém PIS', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_cofins = models.CharField(verbose_name='retém COFINS', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_ir = models.CharField(verbose_name='retém IR', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_csll = models.CharField(verbose_name='retém CSLL', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    dispensa_icms = models.BooleanField(verbose_name='dispensa de ICMS')
    destaque_icms = models.BooleanField(verbose_name='destacar ICMS')

class Endereco(models.Model):
    cnpj = models.CharField(verbose_name='CNPJ do endereço', max_length=20, blank=False, unique=True, db_index=True)
    empresa = models.ForeignKey('Empresa')
    endereco = models.CharField(verbose_name='endereço', max_length=80, default="")
    bairro = models.CharField(verbose_name='bairro', max_length=40, default="")
    cidade = models.CharField(verbose_name='cidade', max_length=40, default="")
    # TODO: verificar lista de UFs
    uf = models.CharField(verbose_name='UF', max_length=2, default="")
    # TODO: verificar opções de consulta de CEP
    cep = models.CharField(verbose_name='CEP', max_length=8, default="")
    inscricao_municipal = models.CharField(verbose_name='inscrição municipal', max_length=20, default="")
    inscricao_estadual = models.CharField(verbose_name='inscrição estadual', max_length=20, default="")
    # TODO: verificar se a inscrição estadual é única para a empresa ou é por 
    # endereço. a inscrição municipal eu já sei que é por endereço.

class Contrato(models.Model):
    cliente = models.ForeignKey('Endereco')

class Aditivo(models.Model):
    empresa = models.ForeignKey('Empresa')

class Circuito(models.Model):
    designacao = models.CharField(verbose_name='designação do circuito', max_length=18, blank=False, unique=True, db_index=True)
    produto = models.ForeignKey('catalogo.Produto')

class Item(models.Model):
    designacao = models.CharField(verbose_name='designação do circuito', max_length=18, blank=False, unique=True, db_index=True)


    # continua amanhã