#coding=utf8

from django.db import models

ESFERA_PRODUTO = (
    ('M', 'Municipal'),
    ('E', 'Estadual'),
    ('F', 'Federal'),
    )

class Produto(models.Model):
    produto = models.CharField(verbose_name='nome do produto', max_length=30, blank=False, unique=True, db_index=True)
    esfera = models.CharField(verbose_name='esfera do produto', max_length=1, blank=False, choices=ESFERA_PRODUTO)
    descricao = models.CharField(verbose_name='descrição do produto', max_length=80, blank=False, unique=True)
    natureza_nf = models.CharField(verbose_name='natureza da NF', max_length=40)
    cfop_estado = models.CharField(verbose_name='CFOP dentro do estado', max_length=4)
    cfop_fora_estado = models.CharField(verbose_name='CFOP fora do estado', max_length=4)
    cnae = models.CharField(verbose_name='CNAE', max_length=12)
    cnae_subitem = models.CharField(verbose_name='subitem CNAE', max_length=10)
    pis = models.DecimalField(verbose_name='PIS', max_digits=6, decimal_places=2)
    cofins = models.DecimalField(verbose_name='COFINS', max_digits=6, decimal_places=2)
    iss = models.DecimalField(verbose_name='ISS', max_digits=6, decimal_places=2)
    icms = models.DecimalField(verbose_name='ICMS', max_digits=6, decimal_places=2)
    inss = models.DecimalField(verbose_name='INSS', max_digits=6, decimal_places=2)
    
    def total_impostos(self):
        return (self.pis + self.cofins + self.iss + self.icms)
