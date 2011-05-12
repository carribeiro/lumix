from catalogo.models import Produto
from django.contrib import admin

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'descricao', 'esfera', 'icms', 'total_impostos')
    list_editable = ('descricao', 'esfera')
    ordering = ('produto', )

admin.site.register(Produto, ProdutoAdmin)