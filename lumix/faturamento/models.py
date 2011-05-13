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
        return  u'%s, %s, %d' % (self.contrato, self.circuito, self.valor)

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
    valor_bruto = models.DecimalField(verbose_name='valor bruto', max_digits=9, decimal_places=2)

#========================
# http://code.activestate.com/recipes/577274-subtract-or-add-a-month-to-a-datetimedate-or-datet/

"""
def subtract_one_month(dt0):
    dt1 = dt0.replace(days=1)
    dt2 = dt1 - timedelta(days=1)
    dt3 = dt2.replace(days=1)
    return dt3

def add_one_month(dt0):
    dt1 = dt0.replace(days=1)
    dt2 = dt1 + timedelta(days=32)
    dt3 = dt2.replace(days=1)
    return dt3

def calcula_limite_ciclo(ciclo, mes, ano):
    import datetime
    result = {}
    result['Mẽs Corrido'] = ()
"""

ciclos_maio = {
    1: {
        'Mês Corrido': ('01/04/2011', '30/04/2011'),
        'Mês Fechado Pós': ('01/04/2011', '30/04/2011' ),
        'Mês Fechado Pré': ('01/05/2011', '31/05/2011'),
    },
    9: {
        'Mês Corrido': ('09/04/2011', '08/05/2011'),
        'Mês Fechado Pós': ('01/04/2011', '30/04/2011' ),
        'Mês Fechado Pré': ('01/05/2011', '31/05/2011'),
    },
    10: {
        'Mês Corrido': ('10/04/2011', '09/05/2011'),
        'Mês Fechado Pós': ('01/04/2011', '30/04/2011' ),
        'Mês Fechado Pré': ('01/05/2011', '31/05/2011'),
    },
    15: {
        'Mês Corrido': ('15/04/2011', '14/05/2011'),
        'Mês Fechado Pós': ('01/04/2011', '30/04/2011' ),
        'Mês Fechado Pré': ('01/05/2011', '31/05/2011'),
    },
    17: {
        'Mês Corrido': ('17/04/2011', '16/05/2011'),
        'Mês Fechado Pós': ('01/04/2011', '30/04/2011' ),
        'Mês Fechado Pré': ('01/05/2011', '31/05/2011'),
    },
}   

def calcula_faturamento():
    ItemFaturado.objects.all().delete()
    for pf in ProvisaoFatura.objects.all():
        ifat = ItemFaturado(provisao_fatura=pf)
        ifat.save()
        ifat.data_inicial = pf.data_inicial
        ifat.data_final = pf.data_final
        ifat.inicio_ciclo, ifat.fim_ciclo= ciclos_maio[pf.ciclo][pf.modalidade]
        #ifat.inicio_fatura
        #ifat.fim_fatura

        produto = pf.produto
        empresa = pf.endereco_faturamento.empresa

        # impostos diretos
        ifat.valor_bruto = pf.valor
        ifat.perc_pis = produto.pis
        ifat.perc_cofins = produto.cofins
        ifat.perc_iss = produto.iss
        ifat.perc_icms = produto.icms
        ifat.val_pis = pf.valor * produto.pis
        ifat.val_cofins = pf.valor * produto.cofins
        ifat.val_iss = pf.valor * produto.iss
        ifat.val_icms = pf.valor * produto.icms

        # retencoes
        if (empresa.retem_pis == 'S') or (empresa.retem_pis == produto.esfera):
            ifat.perc_ret_pis = ifat.perc_pis
            ifat.val_ret_pis = ifat.val_pis
        else:
            ifat.perc_ret_pis = 0
        if (empresa.retem_cofins == 'S') or (empresa.retem_cofins == produto.esfera):
            ifat.perc_ret_cofins = ifat.perc_cofins
            ifat.val_ret_cofins = ifat.val_cofins
        else:
            ifat.perc_ret_cofins = 0
        if (empresa.retem_iss == 'S') or (empresa.retem_iss == produto.esfera):
            ifat.perc_ret_iss = ifat.perc_iss
            ifat.val_ret_iss = ifat.val_iss
        else:
            ifat.perc_ret_iss = 0
        # a tabela de retencao de ir/csll é por cliente e está errada, o campo cadastrado é char e deveria ser decimal
        if (empresa.retem_ir == 'S') or (empresa.retem_ir == produto.esfera):
            ifat.perc_ret_ir = ifat.perc_ir
            ifat.val_ret_ir = ifat.val_ir
        else:
            ifat.perc_ret_ir = 0
        if (empresa.retem_csll == 'S') or (empresa.retem_csll == produto.esfera):
            ifat.perc_ret_csll = ifat.perc_csll
            ifat.val_ret_csll = ifat.val_csll
        else:
            ifat.perc_ret_csll = 0

        ifat.valor_bruto = ifat.valor - ifat.ret_pis - ifat.ret_cofins - \
            ifat.ret_iss - ifat.ret_ir - ifat.csll
