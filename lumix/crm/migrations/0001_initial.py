# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Segmento'
        db.create_table('crm_segmento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_segmento', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('crm', ['Segmento'])

        # Adding model 'Empresa'
        db.create_table('crm_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
            ('porte', self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True)),
            ('razao_social', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60, db_index=True)),
            ('segmento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Segmento'], null=True)),
            ('atividade', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
            ('data_captacao', self.gf('django.db.models.fields.DateField')()),
            ('retem_iss', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_pis', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_cofins', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_ir', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_csll', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('dispensa_icms', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('destaque_icms', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('crm', ['Empresa'])

        # Adding model 'Endereco'
        db.create_table('crm_endereco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, db_index=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Empresa'])),
            ('endereco', self.gf('django.db.models.fields.CharField')(default='', max_length=80)),
            ('bairro', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('cidade', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('uf', self.gf('django.db.models.fields.CharField')(default='', max_length=2)),
            ('cep', self.gf('django.db.models.fields.CharField')(default='', max_length=8)),
            ('inscricao_municipal', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('inscricao_estadual', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
        ))
        db.send_create_signal('crm', ['Endereco'])

        # Adding model 'Contrato'
        db.create_table('crm_contrato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Endereco'])),
        ))
        db.send_create_signal('crm', ['Contrato'])

        # Adding model 'Aditivo'
        db.create_table('crm_aditivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Empresa'])),
        ))
        db.send_create_signal('crm', ['Aditivo'])

        # Adding model 'Circuito'
        db.create_table('crm_circuito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designacao', self.gf('django.db.models.fields.CharField')(unique=True, max_length=18, db_index=True)),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Produto'])),
        ))
        db.send_create_signal('crm', ['Circuito'])

        # Adding model 'Item'
        db.create_table('crm_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designacao', self.gf('django.db.models.fields.CharField')(unique=True, max_length=18, db_index=True)),
        ))
        db.send_create_signal('crm', ['Item'])


    def backwards(self, orm):
        
        # Deleting model 'Segmento'
        db.delete_table('crm_segmento')

        # Deleting model 'Empresa'
        db.delete_table('crm_empresa')

        # Deleting model 'Endereco'
        db.delete_table('crm_endereco')

        # Deleting model 'Contrato'
        db.delete_table('crm_contrato')

        # Deleting model 'Aditivo'
        db.delete_table('crm_aditivo')

        # Deleting model 'Circuito'
        db.delete_table('crm_circuito')

        # Deleting model 'Item'
        db.delete_table('crm_item')


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
        },
        'crm.aditivo': {
            'Meta': {'object_name': 'Aditivo'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.circuito': {
            'Meta': {'object_name': 'Circuito'},
            'designacao': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '18', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalogo.Produto']"})
        },
        'crm.contrato': {
            'Meta': {'object_name': 'Contrato'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Endereco']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'atividade': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'data_captacao': ('django.db.models.fields.DateField', [], {}),
            'destaque_icms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dispensa_icms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porte': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'razao_social': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60', 'db_index': 'True'}),
            'retem_cofins': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_csll': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_ir': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_iss': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_pis': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'segmento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Segmento']", 'null': 'True'})
        },
        'crm.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'bairro': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'cep': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8'}),
            'cidade': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Empresa']"}),
            'endereco': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscricao_estadual': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'inscricao_municipal': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'uf': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2'})
        },
        'crm.item': {
            'Meta': {'object_name': 'Item'},
            'designacao': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '18', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.segmento': {
            'Meta': {'object_name': 'Segmento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_segmento': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crm']
