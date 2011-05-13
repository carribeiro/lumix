#coding=utf8

from django.db import models

class ProvisaoFatura(models.Model):
    contrato = models.ForeignKey('crm.Contrato')
    endereco_faturamento = models.ForeignKey('crm.Endereco')
    circuito = models.ForeignKey('crm.Circuito')
    produto = models.ForeignKey('catalogo.Produto')
    info_adicional = models.CharField(verbose_name='informações adicionais', max_length=60, default="", blank=True, null=True)
    valor = models.DecimalField(verbose_name='valor', max_digits=9, decimal_places=2)
    prazo = models.IntegerField(verbose_name='prazo', default=36, null=True)
    data_inicial = models.DateField(verbose_name='data inicial', null=True)
    data_final = models.DateField(verbose_name='data final', null=True)
    modalidade = models.CharField(verbose_name='modalidade', max_length=20, default="", blank=True)
    ciclo = models.IntegerField(verbose_name='ciclo', default=15, null=True)

    def __unicode__(self):
        return  u'%s, %s, %d' % (self.contrato, self.circuito, valor)
