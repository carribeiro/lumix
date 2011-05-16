#coding=utf8

from django.db import models

class Segmento(models.Model):
    # valores típicos: educação, saúde, governo, etc.
    segmento = models.CharField(verbose_name='nome do segmento', max_length=30)

    def __unicode__(self):
        return  u'%s' % self.segmento

TIPO_RETENCAO_IMPOSTOS = (
    ('S', 'Sempre'), 
    ('N', 'Nunca'), 
    ('E', 'NF Estado'), #'Retém em NFs Estaduais'), 
    ('M', 'NF Município'), #'Retém em NFs Municipais')
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

    def num_circuitos(self):
        return self.circuito_set.count()
    num_circuitos.short_description = '#Circuitos'

    def num_enderecos(self):
        return self.endereco_set.count()
    num_enderecos.short_description = '#Endereços'

    def __unicode__(self):
        return  u'%s: #circuitos:%d, #endereços:%d' % \
            (self.empresa, self.num_circuitos(), self.num_enderecos())

class Endereco(models.Model):
    cnpj = models.CharField(verbose_name='CNPJ do endereço', max_length=20, blank=False, unique=True, db_index=True)
    empresa = models.ForeignKey('Empresa')
    # TODO: razao social não deveria estar no endereço, e sim na empresa. o problema
    # é que hoje em alguns casos o mesmo cliente tem mais de uma razão social,
    # ou seja, empresas diferentes de um mesmo grupo são tratadas como um só cliente.
    razao_social = models.CharField(verbose_name='razão social', max_length=80, blank=False, unique=False, db_index=True)
    endereco = models.CharField(verbose_name='endereço', max_length=80, default="")
    bairro = models.CharField(verbose_name='bairro', max_length=40, default="", null=True)
    cidade = models.CharField(verbose_name='cidade', max_length=40, default="", null=True)
    # TODO: verificar lista de UFs
    uf = models.CharField(verbose_name='UF', max_length=2, default="")
    # TODO: verificar opções de consulta de CEP
    cep = models.CharField(verbose_name='CEP', max_length=8, default="")
    inscricao_municipal = models.CharField(verbose_name='inscrição municipal', max_length=20, default="", null=True)
    inscricao_estadual = models.CharField(verbose_name='inscrição estadual', max_length=20, default="", null=True)
    # TODO: verificar se a inscrição estadual é única para a empresa ou é por 
    # endereço. a inscrição municipal eu já sei que é por endereço.

    def nome_empresa(self):
        return self.empresa.empresa
    nome_empresa.short_description = 'Nome Empresa'

    def __unicode__(self):
        return  u'%s: %s, %s' % \
            (self.cnpj, self.empresa, self.endereco)

class Circuito(models.Model):
    designacao = models.CharField(verbose_name='designação do circuito', max_length=20, blank=False, unique=True, db_index=True)
    produto = models.ForeignKey('catalogo.Produto')
    vlan = models.IntegerField(verbose_name='VLAN', null=True)
    empresa = models.ForeignKey('Empresa')
    sequencia = models.IntegerField(verbose_name='sequência')

    def __unicode__(self):
        return  u'%s: %s, %s, %s' % \
            (self.designacao, self.empresa, self.produto, self.sequencia)

class Contrato(models.Model):
    empresa = models.ForeignKey('Empresa')

    def __unicode__(self):
        return  u'%s: %s' % \
            (self.id, self.empresa)

class ItemContrato(models.Model):
    contrato = models.ForeignKey('Contrato')
    endereco_faturamento = models.ForeignKey('Endereco')
    circuito = models.ForeignKey('Circuito')
    produto = models.ForeignKey('catalogo.Produto')
    info_adicional = models.CharField(verbose_name='informações adicionais', max_length=60, default="", blank=True, null=True)
    valor = models.DecimalField(verbose_name='valor', max_digits=9, decimal_places=2)
    prazo = models.IntegerField(verbose_name='prazo', default=36, null=True)
    data_inicial = models.DateField(verbose_name='data inicial', null=True)
    data_final = models.DateField(verbose_name='data final', null=True)
    modalidade = models.CharField(verbose_name='modalidade', max_length=20, default="", blank=True)
    ciclo = models.IntegerField(verbose_name='ciclo', default=15, null=True)
    # TODO: o ciclo não poderia estar aqui, deveria fazer parte do contrato
    # TODO: será que as ocorrências deveriam estar ligadas a um contrato?
    def __unicode__(self):
        return  u'%s, %s, %s, %s' % \
            (self.endereco_faturamento.empresa.empresa, self.circuito.designacao, self.endereco_faturamento, self.produto)
