# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ProvisaoFatura'
        db.create_table('faturamento_provisaofatura', (
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
        db.send_create_signal('faturamento', ['ProvisaoFatura'])

        # Adding model 'NotaFiscal'
        db.create_table('faturamento_notafiscal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('produto_base', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Produto'])),
            ('endereco_faturamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Endereco'])),
            ('data_pagamento', self.gf('django.db.models.fields.DateField')()),
            ('inicio_fatura', self.gf('django.db.models.fields.DateField')(null=True)),
            ('fim_fatura', self.gf('django.db.models.fields.DateField')(null=True)),
            ('valor_bruto', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('perc_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_icms', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('val_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_icms', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('perc_ret_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_ir', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_csll', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('val_ret_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_ir', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_csll', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('valor_liquido', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('faturamento', ['NotaFiscal'])

        # Adding model 'ItemFaturado'
        db.create_table('faturamento_itemfaturado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provisao_fatura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faturamento.ProvisaoFatura'])),
            ('data_inicial', self.gf('django.db.models.fields.DateField')(null=True)),
            ('data_final', self.gf('django.db.models.fields.DateField')(null=True)),
            ('inicio_ciclo', self.gf('django.db.models.fields.DateField')(null=True)),
            ('fim_ciclo', self.gf('django.db.models.fields.DateField')(null=True)),
            ('inicio_fatura', self.gf('django.db.models.fields.DateField')(null=True)),
            ('fim_fatura', self.gf('django.db.models.fields.DateField')(null=True)),
            ('valor_bruto', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('perc_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_icms', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('val_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_icms', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('perc_ret_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_ir', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('perc_ret_csll', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('val_ret_pis', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_cofins', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_iss', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_ir', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('val_ret_csll', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('valor_liquido', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('faturamento', ['ItemFaturado'])


    def backwards(self, orm):
        
        # Deleting model 'ProvisaoFatura'
        db.delete_table('faturamento_provisaofatura')

        # Deleting model 'NotaFiscal'
        db.delete_table('faturamento_notafiscal')

        # Deleting model 'ItemFaturado'
        db.delete_table('faturamento_itemfaturado')


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
        'crm.segmento': {
            'Meta': {'object_name': 'Segmento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segmento': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'faturamento.itemfaturado': {
            'Meta': {'object_name': 'ItemFaturado'},
            'data_final': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'data_inicial': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fim_ciclo': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fim_fatura': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio_ciclo': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'inicio_fatura': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'perc_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_icms': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_csll': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_ir': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'provisao_fatura': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['faturamento.ProvisaoFatura']"}),
            'val_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_icms': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_csll': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_ir': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'valor_bruto': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'valor_liquido': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'faturamento.notafiscal': {
            'Meta': {'object_name': 'NotaFiscal'},
            'data_pagamento': ('django.db.models.fields.DateField', [], {}),
            'endereco_faturamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Endereco']"}),
            'fim_fatura': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio_fatura': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'perc_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_icms': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_csll': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_ir': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'perc_ret_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'produto_base': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalogo.Produto']"}),
            'val_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_icms': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_cofins': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_csll': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_ir': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_iss': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'val_ret_pis': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'valor_bruto': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'valor_liquido': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'faturamento.provisaofatura': {
            'Meta': {'object_name': 'ProvisaoFatura'},
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
        }
    }

    complete_apps = ['faturamento']
