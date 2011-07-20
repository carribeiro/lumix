from django.conf.urls.defaults import *
from crm.views import ListViewEmpresas, DetailViewEmpresa, CreateViewEmpresa, UpdateViewEmpresa

urlpatterns = patterns('',
    (r'^empresas/$', ListViewEmpresas.as_view()),
    (r'^empresas/(?P<pk>\w+)/$', DetailViewEmpresa.as_view()),
    (r'^empresas/(?P<pk>\w+)/edit$', UpdateViewEmpresa.as_view()),
    (r'^empresas/(?P<pk>\w+)/add$', CreateViewEmpresa.as_view()),
)
