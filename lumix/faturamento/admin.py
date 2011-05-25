from faturamento.models import DataCalendario, CicloFaturamentoDefault, \
                               CicloFaturamento, ProvisaoFatura, LoteFaturamento, \
                               NotaFiscal, ItemFaturado, Duplicata
from django.contrib import admin

class DataCalendarioAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao', 'feriado')

class CicloFaturamentoDefaultAdmin(admin.ModelAdmin):
    list_display = ('dia_faturamento', 'dia_venc_default')

class CicloFaturamentoAdmin(admin.ModelAdmin):
    list_display = ('ciclo', 'data_faturamento', 'data_vencimento',
                    'dt_mes_corr_ini', 'dt_mes_corr_fim', 'dt_mes_fpre_ini',
                    'dt_mes_fpre_fim', 'dt_mes_fpos_ini', 'dt_mes_fpos_fim', )

class ProvisaoFaturaAdmin(admin.ModelAdmin):
    #list_display = ('contrato', 'endereco_faturamento__cnpj', 'endereco_faturamento__razao_social', 'circuito', 'produto')
    list_display = ('contrato', 'endereco_faturamento', 'circuito', 'produto')
    #ordering = ('endereco_faturamento__empresa__seq_designacao', 'circuito__sequencia', 'circuito__designacao')

class LoteFaturamentoAdmin(admin.ModelAdmin):
    list_display = ('data_faturamento', 'tipo_lote', 'ciclo', 'status', )

class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('numero', 'lote', 'endereco_faturamento', 'data_pagamento', 
                    'inicio_fatura', 'fim_fatura', 'valor_bruto', 'valor_liquido', )

class ItemFaturadoAdmin(admin.ModelAdmin):
    list_display = ('provisao_fatura', 'nota_fiscal', 'valor_liquido', )

class DuplicataAdmin(admin.ModelAdmin):
    list_display = ('nota_fiscal', 'data_pagamento', 'valor', )

admin.site.register(DataCalendario, DataCalendarioAdmin)
admin.site.register(CicloFaturamentoDefault, CicloFaturamentoDefaultAdmin)
admin.site.register(CicloFaturamento, CicloFaturamentoAdmin)
admin.site.register(ProvisaoFatura, ProvisaoFaturaAdmin)
admin.site.register(LoteFaturamento, LoteFaturamentoAdmin)
admin.site.register(NotaFiscal, NotaFiscalAdmin)
admin.site.register(ItemFaturado, ItemFaturadoAdmin)
admin.site.register(Duplicata, DuplicataAdmin)