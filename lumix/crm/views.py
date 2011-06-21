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

@login_required
def cliente(request):
    return render_to_response('cliente.html', {
    #        'main_form': main_form,
    }, context_instance=RequestContext(request))

from django.views.generic import ListView
from crm.models import Empresa

class CustomerListView(ListView):
    template_name = 'empresa_list.html'
    model = Empresa
    context_object_name = "empresas"
    paginate_by = 10


