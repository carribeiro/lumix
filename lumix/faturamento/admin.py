from faturamento.models import ProvisaoFatura
from django.contrib import admin

class ProvisaoFaturaAdmin(admin.ModelAdmin):
    #list_display = ('contrato', 'endereco_faturamento__cnpj', 'endereco_faturamento__razao_social', 'circuito', 'produto')
    list_display = ('contrato', 'endereco_faturamento', 'circuito', 'produto')
    #ordering = ('endereco_faturamento__empresa__seq_designacao', 'circuito__sequencia', 'circuito__designacao')

admin.site.register(ProvisaoFatura, ProvisaoFaturaAdmin)