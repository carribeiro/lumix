#coding: utf-8

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from crm.models import Empresa
from django.forms import ModelForm

class FormEmpresa(ModelForm):
    class Meta:
        Model = Empresa

class ListViewEmpresas(ListView):
    template_name = 'listview_empresa.html'
    model = Empresa
    context_object_name = "empresas"
    paginate_by = 20

class DetailViewEmpresa(DetailView):
    template_name = 'detailview_empresa.html'
    model = Empresa
    context_object_name = "empresa"

class CreateViewEmpresa(CreateView):
    template_name = 'createview_empresa.html'
    model = Empresa
    context_object_name = "empresa"
    model_class = FormEmpresa
    success_url = ''
    initial = {'empresa': '*teste*'}

class UpdateViewEmpresa(UpdateView):
    template_name = 'updateview_empresa.html'
    model = Empresa
    context_object_name = "empresa"
    form_class = FormEmpresa
    success_url = ''
    initial = {'empresa': '*teste*'}



