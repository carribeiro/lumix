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

class ItemFaturado(models.Model):
    provisao_fatura = models.ForeignKey('faturamento.ProvisaoFatura')
    data_inicial = models.DateField(verbose_name='data inicial', null=True)
    data_final = models.DateField(verbose_name='data final', null=True)
    inicio_ciclo = models.DateField(verbose_name='início do ciclo', null=True)
    fim_ciclo = models.DateField(verbose_name='final do ciclo', null=True)
    inicio_fatura = models.DateField(verbose_name='início do período de fatura', null=True)
    fim_fatura = models.DateField(verbose_name='final do período de fatura', null=True)
    valor_bruto = models.DecimalField(verbose_name='valor', max_digits=9, decimal_places=2)
    perc_pis = models.DecimalField(verbose_name='%PIS', max_digits=6, decimal_places=2)
    perc_cofins = models.DecimalField(verbose_name='%COFINS', max_digits=6, decimal_places=2)
    perc_iss = models.DecimalField(verbose_name='%ISS', max_digits=6, decimal_places=2)
    perc_icms = models.DecimalField(verbose_name='%ICMS', max_digits=6, decimal_places=2)
    val_pis = models.DecimalField(verbose_name='$PIS', max_digits=9, decimal_places=2)
    val_cofins = models.DecimalField(verbose_name='$COFINS', max_digits=9, decimal_places=2)
    val_iss = models.DecimalField(verbose_name='$ISS', max_digits=9, decimal_places=2)
    val_icms = models.DecimalField(verbose_name='$ICMS', max_digits=9, decimal_places=2)
    perc_ret_pis = models.DecimalField(verbose_name='%PIS', max_digits=6, decimal_places=2)
    perc_ret_cofins = models.DecimalField(verbose_name='%COFINS', max_digits=6, decimal_places=2)
    perc_ret_iss = models.DecimalField(verbose_name='%ISS', max_digits=6, decimal_places=2)
    perc_ret_ir = models.DecimalField(verbose_name='%IR', max_digits=6, decimal_places=2)
    perc_ret_csll = models.DecimalField(verbose_name='%CSLL', max_digits=6, decimal_places=2)
    val_ret_pis = models.DecimalField(verbose_name='%PIS', max_digits=9, decimal_places=2)
    val_ret_cofins = models.DecimalField(verbose_name='%COFINS', max_digits=9, decimal_places=2)
    val_ret_iss = models.DecimalField(verbose_name='%ISS', max_digits=9, decimal_places=2)
    val_ret_ir = models.DecimalField(verbose_name='%IR', max_digits=9, decimal_places=2)
    val_ret_csll = models.DecimalField(verbose_name='%CSLL', max_digits=9, decimal_places=2)
    valor_bruto = models.DecimalField(verbose_name='valor', max_digits=9, decimal_places=2)

