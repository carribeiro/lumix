#coding=utf8

import os
import logging

from django.conf import settings
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext, \
    get_object_or_404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from faturamento.models import NotaFiscal

@login_required
def notas_fiscais(request):
    return render_to_response('notas_fiscais.html', context_instance=RequestContext(request))

@login_required
def notas_fiscais_estaduais(request):
    return render_to_response('notas_fiscais_estaduais.html', context_instance=RequestContext(request))

@login_required
def notas_fiscais_municipais(request):
    return render_to_response('notas_fiscais_municipais.html', context_instance=RequestContext(request))

@login_required
def nota_fiscal(request, num_nf):
    nf = NotaFiscal.objects.get(num_nf)
    if nf.produto_base.esfera == "M":
        return render_to_response('nota_fiscal_estado.html', {'nf': nf}, context_instance=RequestContext(request))
    elif nf.produto_base.esfera == "M":
        return render_to_response('nota_fiscal_estado.html', {'nf': nf}, context_instance=RequestContext(request))
    else:
        return render_to_response('nota_fiscal_erro.html', {'nf': nf}, context_instance=RequestContext(request))
