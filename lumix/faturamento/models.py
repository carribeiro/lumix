#coding=utf8

from django.db import models

# TODO: vou implementar o processo em fases. 
#  1) abre o ciclo
#  2) seleciona itens para faturar

# todo: coisas pra estudar: proxy model, abstract model.

class DataCalendario(models.Model):
    data = models.DateField(verbose_name='data', unique=True, db_index=True)
    descricao = models.CharField(verbose_name='descrição', max_length=60, blank=True, default='')
    feriado = models.BooleanField(verbose_name='feriado?', default=True) 

def feriado(data):
    try:
        data_calendario = DataCalendario.get(data=data)
        return data_calendario.feriado
    except:
        return False

def dia_util(data):
    import datetime
    return not (feriado(data) or (datetime.weekday(data) in [0,6]))

class CicloFaturamentoDefault(models.Model):
    """ Define os parâmetros default para um ciclo de faturamento.
    """
    dia_faturamento = models.IntegerField(verbose_name='dia de faturamento', unique=True, db_index=True)
    dia_venc_default = models.IntegerField(verbose_name='dia default de vencimento', )

# Observacoes sobre uma decisão de design: o processo de faturamento 
# está sendo pensado etapa a etapa, o que exige entidades intermediarias.
# O espaço e a performance podem ser inferiores, mas o desenvolvimento
# fica mais simples. O maior risco desse tipo de abordagem vem a longo
# prazo pois é possívell que a base de dados fique inconsistente, o que
# torna necessário desenvolver rotinas adicionais de conciliação.

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

class CicloFaturamento(models.Model):
    """ Define um ciclo de faturamento real. Quando o ciclo é criado, as
        datas de cada tipo de contrato (corrido, fechado pré ou fechado 
        pós) são calculadas, bem como a data default de vencimento de todos
        as faturas do ciclo. Os períodos a faturar são provisionados para
        pagamento.
    """
    ciclo = models.ForeignKey('faturamento.CicloFaturamentoDefault')
    data_faturamento = models.DateField(verbose_name='data de faturamento')
    data_vencimento = models.DateField(verbose_name='data de vencimento')
    dt_mes_corr_ini = models.DateField(verbose_name='data inicial mês corrido')
    dt_mes_corr_fim = models.DateField(verbose_name='data final mês corrido')
    dt_mes_fpre_ini = models.DateField(verbose_name='data inicial mês fechado pré')
    dt_mes_fpre_fim = models.DateField(verbose_name='data final mês fechado pré')
    dt_mes_fpos_ini = models.DateField(verbose_name='data inicial mês fechado pós')
    dt_mes_fpos_fim = models.DateField(verbose_name='data final mês fechado pós')

TIPO_LOTE_FATURAMENTO = (
    ('C', 'Ciclo'), 
    ('A', 'Avulso'), 
    # pode ser que surjam mais tipos depois (ex: lotes de cancelamento, ajuste, etc.)
    )

STATUS_LOTE_FATURAMENTO = (
    ('Calculado', 'Calculado'), 
    ('Conferido', 'Conferido'), 
    ('Impresso', 'Impresso'), 
    ('Cancelado', 'Cancelado'), # Nem sei se faz sentido cancelar um lote, ou apenas deletar do BD...
    )

class LoteFaturamento(models.Model):
    """ 
    Equivale a um lote de NFs emitidas em uma determinada data.

    Existem dois tipos básicos de lote: os lotes de "ciclo" serve para 
    faturar todos os contratos de uma certa data (igual ao número do 
    ciclo). Também existem ciclos "avulsos". Pode ser que no mesmo dia 
    de um ciclo, depois do ciclo emitido, seja criado um novo lote com 
    notas avulsas.

    TODO: talvez seja o caso de faturar as ocorrências em um lote separado.
    Acho que faria sentido...

    Notas:
    - A data do ciclo não precisa necessariamente coincidir com a data
      de faturamento, devido a feriados e outros eventos do tipo.
    - Um lote pode ter faturas que vençam em datas diferentes.
    """
    data_faturamento = models.DateField(verbose_name='data de faturamento')
    tipo_lote = models.CharField(verbose_name='tipo do lote', max_length=1, choices=TIPO_LOTE_FATURAMENTO)
    ciclo = models.ForeignKey('CicloFaturamento', null=True)  # lotes avulsos não se referem a um ciclo
    status = models.CharField(verbose_name='status do lote', max_length=15, choices=STATUS_LOTE_FATURAMENTO)

class NotaFiscal(models.Model):
    lote = models.ForeignKey('LoteFaturamento')
    numero = models.IntegerField(verbose_name='NF', default=0, null=True)
    # a mesma NF pode até ter produtos diferentes, mas desde que compartilhem classificação parecida
    produto_base = models.ForeignKey('catalogo.Produto')
    endereco_faturamento = models.ForeignKey('crm.Endereco')
    data_pagamento = models.DateField(verbose_name='data pagamento', null=False)

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
    valor_liquido = models.DecimalField(verbose_name='valor líquido', max_digits=9, decimal_places=2)


class ItemFaturado(models.Model):
    provisao_fatura = models.ForeignKey('faturamento.ProvisaoFatura')
    nota_fiscal = models.ForeignKey('faturamento.NotaFiscal')
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
    valor_liquido = models.DecimalField(verbose_name='valor líquido', max_digits=9, decimal_places=2)

    def __unicode__(self):
        return  u'%s, %s' % (self.provisao_fatura.circuito.designacao, self.valor)

STATUS_DUPLICATA = (
    ('Calculada', 'Calculada'), 
    ('Exportada', 'Exportada'), # A duplicata pode ser exportada depois da impressão da NF 
    ('Cancelada', 'Cancelada'), # Nem sei se faz sentido cancelar um lote, ou apenas deletar do BD...
    )

class Duplicata(models.Model):
    nota_fiscal = models.ForeignKey('faturamento.NotaFiscal')
    data_pagamento = models.DateField(verbose_name='data pagamento', null=False)
    valor = models.DecimalField(verbose_name='valor a pagar', max_digits=9, decimal_places=2)

#========================
# ROTINAS DE TESTE E DESENVOLVIMENTO
#
# Para a primeira versão do sistema, vamos rodar um faturamento manualmente, desenvolvendo
# rotinas que depois serão refatoradas e integradas/sequenciadas na interface Web.

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

def date_dma(strdate):
    import datetime
    return datetime.datetime.strptime(strdate, "%d/%m/%Y").strftime('%Y-%m-%d')

#tipos_faturamento = {
#    'Mês Corrido'
#    'Mês Fechado Pós'
#    'Mês Fechado Pré'
#}

ciclos_maio = {
    1: {
        'Mês Corrido': (date_dma('01/04/2011'),date_dma('30/04/2011')),
        'Mês Fechado Pós': (date_dma('01/04/2011'),date_dma('30/04/2011')),
        'Mês Fechado Pré': (date_dma('01/05/2011'),date_dma('31/05/2011')),
    },
    9: {
        'Mês Corrido': (date_dma('09/04/2011'),date_dma('08/05/2011')),
        'Mês Fechado Pós': (date_dma('01/04/2011'),date_dma('30/04/2011')),
        'Mês Fechado Pré': (date_dma('01/05/2011'),date_dma('31/05/2011')),
    },
    10: {
        'Mês Corrido': (date_dma('10/04/2011'),date_dma('09/05/2011')),
        'Mês Fechado Pós': (date_dma('01/04/2011'),date_dma('30/04/2011')),
        'Mês Fechado Pré': (date_dma('01/05/2011'),date_dma('31/05/2011')),
    },
    15: {
        'Mês Corrido': (date_dma('15/04/2011'),date_dma('14/05/2011'),date_dma('05/06/2011')),
        'Mês Fechado Pós': (date_dma('01/04/2011'),date_dma('30/04/2011'),date_dma('05/06/2011')),
        'Mês Fechado Pré': (date_dma('01/05/2011'),date_dma('31/05/2011'),date_dma('05/06/2011')),
    },
    17: {
        'Mês Corrido': (date_dma('17/04/2011'),date_dma('16/05/2011')),
        'Mês Fechado Pós': (date_dma('01/04/2011'),date_dma('30/04/2011')),
        'Mês Fechado Pré': (date_dma('01/05/2011'),date_dma('31/05/2011')),
    },
}   

def calcula_faturamento():
    # para a primeira versão de desenvolvimento, zera o banco de dados de faturamento. 
    ItemFaturado.objects.all().delete()
    CicloFaturamentoDefault.objects.all().delete()
    CicloFaturamento.objects.all().delete()

    # cria os ciclos de faturamento default
    # TODO!!

    # cria os ciclos de faturamento de maio, usando os dados pré-calculados
    # TODO!!

    # cria os lotes de faturamento de maio
    # TODO!!

    # inicializa contador de NFs com o numero da proxima NF a ser criada. 
    # TODO: isso acelera o processo mas não é threadsafe 
    if NotaFiscal.objects.count() == 0:
        proxima_nf = 1
    else:
        from django.db.models import Max
        proxima_nf = NotaFiscal.objects.aggregate.Max('numero')['numero__max'] + 1

    # percorre todas as provisoes de fatura
    # TODO: na planilha excel, para facilitar o agrupamento por NF, o dataset original de provisao_fatura era
    # ordenado por tipo de NF+cnpj, o que já deixava as coisas agrupadas de forma correta. podemos fazer algo
    # parecido aqui também.
    for pf in ProvisaoFatura.objects.all():
        # procura a NF do ciclo para o cliente, e se não achar, cria uma nova NF

        # a NF agrupa produtos do mesmo ciclo, do mesmo endereço, da mesma esfera, e deve ter um produto base compatível
        # TODO: criar um campo com "grupo-produto" para facilitar a busca de produtos compatíveis

        nf_candidata = list(NotaFiscal.objects.filter(endereco_faturamento=pf.endereco_faturamento, produto_base__esfera=pf.produto.esfera))
        # TODO: testar tb a data_pagamento
        if len(nf.candidata) > 1:
            # TODO: tratar este erro
            nf = nf_candidata[0]
        elif len(nf.candidata) == 1:
            nf = nf_candidata[0]
        else:
            # cria uma nova NF para o produto a faturar
            from decimal import Decimal
            # verifica ciclo & calcula datas
            # TODO: teste simples, coloca todo mundo no dia 15 com mes_fechado_pre
            inicio_fatura, fim_datura, data_pagamento = ciclos_maio[15]['Mês Fechado Pré']
            # cria a NF
            nf = NotaFiscal(
                numero = proxima_nf,
                produto_base = pf.produto,
                endereco_faturamento = pf.endereco,
                data_pagamento = data_pagamento,
                inicio_fatura = inicio_fatura,
                fim_fatura = fim_fatura,
                valor_bruto = Decimal('0.00'),
                perc_pis = Decimal('0.00'),
                perc_cofins = Decimal('0.00'),
                perc_iss = Decimal('0.00'),
                perc_icms = Decimal('0.00'),
                val_pis = Decimal('0.00'),
                val_cofins = Decimal('0.00'),
                val_iss = Decimal('0.00'),
                val_icms = Decimal('0.00'),
                perc_ret_pis = Decimal('0.00'),
                perc_ret_cofins = Decimal('0.00'),
                perc_ret_iss = Decimal('0.00'),
                perc_ret_ir = Decimal('0.00'),
                perc_ret_csll = Decimal('0.00'),
                val_ret_pis = Decimal('0.00'),
                val_ret_cofins = Decimal('0.00'),
                val_ret_iss = Decimal('0.00'),
                val_ret_ir = Decimal('0.00'),
                val_ret_csll = Decimal('0.00'),
                valor_liquido = Decimal('0.00'),
            )
            proxima_nf += 1

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
