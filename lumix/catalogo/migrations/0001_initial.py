# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Produto'
        db.create_table('catalogo_produto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('produto', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60, db_index=True)),
            ('esfera', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('natureza_nf', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('cfop_estado', self.gf('django.db.models.fields.CharField')(default='', max_length=4, null=True, blank=True)),
            ('cfop_fora_estado', self.gf('django.db.models.fields.CharField')(default='', max_length=4, null=True, blank=True)),
            ('cnae', self.gf('django.db.models.fields.CharField')(default='', max_length=12, null=True, blank=True)),
            ('cnae_subitem', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True, blank=True)),
            ('pis', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('iss', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('icms', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('inss', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('catalogo', ['Produto'])


    def backwards(self, orm):
        
        # Deleting model 'Produto'
        db.delete_table('catalogo_produto')


    models = {
        'catalogo.produto': {
            'Meta': {'object_name': 'Produto'},
            'cfop_estado': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'cfop_fora_estado': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'cnae': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'cnae_subitem': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'esfera': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'icms': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inss': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'natureza_nf': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'produto': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60', 'db_index': 'True'})
        }
    }

    complete_apps = ['catalogo']
