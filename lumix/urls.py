from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lumix.views.home', name='home'),
    # url(r'^lumix/', include('lumix.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    url(r'^crm/', include('crm.urls')),

    url(r'^$', 'base.views.main', name='main_page'),
    url(r'^nf/$', 'faturamento.views.notas_fiscais', name='notas_fiscais'),
    url(r'^nfestad/$', 'faturamento.views.notas_fiscais_estaduais', name='notas_fiscais_estaduais'),
    url(r'^nfmunic/$', 'faturamento.views.notas_fiscais_municipais', name='notas_fiscais_municipais'),
    url(r'^nf/([0-9]+)/$', 'faturamento.views.nota_fiscal', name='notas_fiscais_estaduais'),
    url(r'^faturamento/$', 'faturamento.views.ciclos_faturamento', name='ciclos_faturamento'),
    url(r'^cliente/$', 'crm.views.lista_clientes', name='lista_clientes'),
    url(r'^cliente/(\w+)/$', 'crm.views.tela_cliente', name='tela_cliente'),
)
