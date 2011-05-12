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
    seq_designacao = models.IntegerField(verbose_name='sequência de designação', unique=True, null=True, db_index=True)
    porte = models.CharField(verbose_name='porte', max_length=15,
                choices=(('-', 'Desconhecido'), ('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')), 
                blank=False, default='-')
    segmento = models.ForeignKey('Segmento', null=True) 
    # os campos a seguir pode ter os valores: N (não), S (sim), M (somente NF municipal), E (somente NF estadual)
    retem_iss = models.CharField(verbose_name='retém ISS', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_pis = models.CharField(verbose_name='retém PIS', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_cofins = models.CharField(verbose_name='retém COFINS', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_ir = models.CharField(verbose_name='retém IR', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    retem_csll = models.CharField(verbose_name='retém CSLL', max_length=1, choices=TIPO_RETENCAO_IMPOSTOS)
    dispensa_icms = models.BooleanField(verbose_name='dispensa de ICMS')
    destaque_icms = models.BooleanField(verbose_name='destacar ICMS')
    nf_separada = models.BooleanField(verbose_name='emitir NF separada')

class Endereco(models.Model):
    cnpj = models.CharField(verbose_name='CNPJ do endereço', max_length=20, blank=False, unique=True, db_index=True)
    empresa = models.ForeignKey('Empresa')
    razao_social = models.CharField(verbose_name='razão social', max_length=60, blank=False, unique=True, db_index=True)
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

class Circuito(models.Model):
    designacao = models.CharField(verbose_name='designação do circuito', max_length=18, blank=False, unique=True, db_index=True)
    produto = models.ForeignKey('catalogo.Produto')
    vlan = models.IntegerField(verbose_name='VLAN', null=True)
    empresa = models.ForeignKey('Empresa')

class Contrato(models.Model):
    empresa = models.ForeignKey('Empresa')

class ItemContrato(models.Model):
    contrato = models.ForeignKey('Contrato')
    endereco_faturamento = models.ForeignKey('Endereco')
    circuito = models.ForeignKey('Circuito')
    info_adicional = models.CharField(verbose_name='informações adicionais', max_length=60, default="", blank=True)
    valor = models.DecimalField(verbose_name='valor', max_digits=9, decimal_places=2)
    prazo = models.IntegerField(verbose_name='prazo', default=36)
    data_inicial = models.DateField(verbose_name='data inicial', null=True)
    data_final = models.DateField(verbose_name='data final', null=True)
    modalidade = models.CharField(verbose_name='modalidade', max_length=20, default="", blank=True)
    ciclo = models.IntegerField(verbose_name='ciclo', default=15)

