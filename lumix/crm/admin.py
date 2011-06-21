#coding=utf8

from crm.models import Segmento, Empresa, Endereco, Circuito, Contrato, ItemContrato
from django.contrib import admin

class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'segmento', )
    list_editable = ('segmento', )
    ordering = ('segmento', )

class EmpresaAdmin(admin.ModelAdmin):
    # estava gerando excesso de queries para agregação um por um em num_circuitos
    #list_display = ('empresa', 'num_circuitos', 'seq_designacao', 'porte', 'segmento', 'retem_iss', 'retem_pis', 'retem_cofins', 'retem_ir', 'retem_csll', 'dispensa_icms', 'destaque_icms')
    list_display = ('empresa', 'seq_designacao', 'porte', 'segmento', 'retem_iss', 'retem_pis', 'retem_cofins', 'retem_ir', 'retem_csll', 'dispensa_icms', 'destaque_icms')
    list_editable = ('porte', 'segmento', 'retem_iss', 'retem_pis', 'retem_cofins', 'retem_ir', 'retem_csll', 'dispensa_icms', 'destaque_icms')
    ordering = ('empresa', )
    search_fields = ['empresa']

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'cnpj', 'razao_social', 'bairro', 'cidade', 'uf', 'cep', 'inscricao_municipal', 'inscricao_estadual')
    list_editable = ('cnpj', 'razao_social', 'bairro', 'cidade', 'uf', 'cep', 'inscricao_municipal', 'inscricao_estadual')
    ordering = ('empresa', 'cnpj', )
    search_fields = ['empresa', 'endereco']

class CircuitoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'produto', 'sequencia', 'designacao')
    #ordering = ('empresa', 'sequencia', )

class ContratoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Segmento, SegmentoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Circuito, CircuitoAdmin)
admin.site.register(Contrato, ContratoAdmin)