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
            ('segmento', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('crm', ['Segmento'])

        # Adding model 'Empresa'
        db.create_table('crm_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
            ('seq_designacao', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, db_index=True)),
            ('porte', self.gf('django.db.models.fields.CharField')(default='-', max_length=15)),
            ('segmento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Segmento'], null=True)),
            ('retem_iss', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_pis', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_cofins', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_ir', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('retem_csll', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('dispensa_icms', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('destaque_icms', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nf_separada', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('crm', ['Empresa'])

        # Adding model 'Endereco'
        db.create_table('crm_endereco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, db_index=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Empresa'])),
            ('razao_social', self.gf('django.db.models.fields.CharField')(max_length=80, db_index=True)),
            ('endereco', self.gf('django.db.models.fields.CharField')(default='', max_length=80)),
            ('bairro', self.gf('django.db.models.fields.CharField')(default='', max_length=40, null=True)),
            ('cidade', self.gf('django.db.models.fields.CharField')(default='', max_length=40, null=True)),
            ('uf', self.gf('django.db.models.fields.CharField')(default='', max_length=2)),
            ('cep', self.gf('django.db.models.fields.CharField')(default='', max_length=8)),
            ('inscricao_municipal', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True)),
            ('inscricao_estadual', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True)),
        ))
        db.send_create_signal('crm', ['Endereco'])

        # Adding model 'Circuito'
        db.create_table('crm_circuito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designacao', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, db_index=True)),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Produto'])),
            ('vlan', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Empresa'])),
            ('sequencia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('crm', ['Circuito'])

        # Adding model 'Contrato'
        db.create_table('crm_contrato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Empresa'])),
        ))
        db.send_create_signal('crm', ['Contrato'])

        # Adding model 'ItemContrato'
        db.create_table('crm_itemcontrato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contrato', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Contrato'])),
            ('endereco_faturamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Endereco'])),
            ('circuito', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Circuito'])),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Produto'])),
            ('info_adicional', self.gf('django.db.models.fields.CharField')(default='', max_length=60, null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('prazo', self.gf('django.db.models.fields.IntegerField')(default=36, null=True)),
            ('data_inicial', self.gf('django.db.models.fields.DateField')(null=True)),
            ('data_final', self.gf('django.db.models.fields.DateField')(null=True)),
            ('modalidade', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('ciclo', self.gf('django.db.models.fields.IntegerField')(default=15, null=True)),
        ))
        db.send_create_signal('crm', ['ItemContrato'])


    def backwards(self, orm):
        
        # Deleting model 'Segmento'
        db.delete_table('crm_segmento')

        # Deleting model 'Empresa'
        db.delete_table('crm_empresa')

        # Deleting model 'Endereco'
        db.delete_table('crm_endereco')

        # Deleting model 'Circuito'
        db.delete_table('crm_circuito')

        # Deleting model 'Contrato'
        db.delete_table('crm_contrato')

        # Deleting model 'ItemContrato'
        db.delete_table('crm_itemcontrato')


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
        'crm.circuito': {
            'Meta': {'object_name': 'Circuito'},
            'designacao': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalogo.Produto']"}),
            'sequencia': ('django.db.models.fields.IntegerField', [], {}),
            'vlan': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'crm.contrato': {
            'Meta': {'object_name': 'Contrato'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'destaque_icms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dispensa_icms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nf_separada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porte': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '15'}),
            'retem_cofins': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_csll': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_ir': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_iss': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retem_pis': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'segmento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Segmento']", 'null': 'True'}),
            'seq_designacao': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'crm.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'bairro': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'null': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8'}),
            'cidade': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'null': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Empresa']"}),
            'endereco': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscricao_estadual': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'inscricao_municipal': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'razao_social': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_index': 'True'}),
            'uf': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2'})
        },
        'crm.itemcontrato': {
            'Meta': {'object_name': 'ItemContrato'},
            'ciclo': ('django.db.models.fields.IntegerField', [], {'default': '15', 'null': 'True'}),
            'circuito': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Circuito']"}),
            'contrato': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contrato']"}),
            'data_final': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'data_inicial': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'endereco_faturamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Endereco']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_adicional': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'modalidade': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'prazo': ('django.db.models.fields.IntegerField', [], {'default': '36', 'null': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalogo.Produto']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'crm.segmento': {
            'Meta': {'object_name': 'Segmento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segmento': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crm']
