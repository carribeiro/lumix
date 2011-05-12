#coding=utf8

from django.db import models
from django.forms.models import model_to_dict

ESFERA_PRODUTO = (
    ('M', 'Municipal'),
    ('E', 'Estadual'),
    ('F', 'Federal'),
    )

class Produto(models.Model):
    produto = models.CharField(verbose_name='nome do produto', max_length=60, blank=False, unique=True, db_index=True)
    esfera = models.CharField(verbose_name='esfera do produto', max_length=1, blank=False, choices=ESFERA_PRODUTO)
    descricao = models.CharField(verbose_name='descrição do produto', max_length=120, blank=False)
    natureza_nf = models.CharField(verbose_name='natureza da NF', max_length=60)
    cfop_estado = models.CharField(verbose_name='CFOP dentro do estado', max_length=4, blank=True, default="", null=True)
    cfop_fora_estado = models.CharField(verbose_name='CFOP fora do estado', max_length=4, blank=True, default="", null=True)
    cnae = models.CharField(verbose_name='CNAE', max_length=12, blank=True, default="", null=True)
    cnae_subitem = models.CharField(verbose_name='subitem CNAE', max_length=10, blank=True, default="", null=True)
    pis = models.DecimalField(verbose_name='PIS', max_digits=6, decimal_places=2)
    cofins = models.DecimalField(verbose_name='COFINS', max_digits=6, decimal_places=2)
    iss = models.DecimalField(verbose_name='ISS', max_digits=6, decimal_places=2)
    icms = models.DecimalField(verbose_name='ICMS', max_digits=6, decimal_places=2)
    inss = models.DecimalField(verbose_name='INSS', max_digits=6, decimal_places=2)
    
    def _get_total_impostos(self):
        return self.pis + self.cofins + self.iss + self.icms
    total_impostos = property(_get_total_impostos)

    def __unicode__(self):
        #return u'%(produto)s %(descricao)s Esfera:%(esfera)s Total de impostos diretos:%(total_impostos)s' % model_to_dict(self, "total_impostos")
        return  u'%s: %s, %s, Tot.impostos:%s%%' % \
            (self.produto, self.descricao, self.get_esfera_display(), self.total_impostos)
