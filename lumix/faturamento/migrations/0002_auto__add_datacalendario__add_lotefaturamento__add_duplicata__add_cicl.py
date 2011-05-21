# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DataCalendario'
        db.create_table('faturamento_datacalendario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateField')(unique=True, db_index=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
            ('feriado', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('faturamento', ['DataCalendario'])

        # Adding model 'LoteFaturamento'
        db.create_table('faturamento_lotefaturamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_faturamento', self.gf('django.db.models.fields.DateField')()),
            ('tipo_lote', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ciclo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faturamento.CicloFaturamento'], null=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('faturamento', ['LoteFaturamento'])

        # Adding model 'Duplicata'
        db.create_table('faturamento_duplicata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nota_fiscal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faturamento.NotaFiscal'])),
            ('data_pagamento', self.gf('django.db.models.fields.DateField')()),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('faturamento', ['Duplicata'])

        # Adding model 'CicloFaturamentoDefault'
        db.create_table('faturamento_ciclofaturamentodefault', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dia_faturamento', self.gf('django.db.models.fields.IntegerField')(unique=True, db_index=True)),
            ('dia_venc_default', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('faturamento', ['CicloFaturamentoDefault'])

        # Adding model 'CicloFaturamento'
        db.create_table('faturamento_ciclofaturamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciclo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faturamento.CicloFaturamentoDefault'])),
            ('data_faturamento', self.gf('django.db.models.fields.DateField')()),
            ('data_vencimento', self.gf('django.db.models.fields.DateField')()),
            ('dt_mes_corr_ini', self.gf('django.db.models.fields.DateField')()),
            ('dt_mes_corr_fim', self.gf('django.db.models.fields.DateField')()),
            ('dt_mes_fpre_ini', self.gf('django.db.models.fields.DateField')()),
            ('dt_mes_fpre_fim', self.gf('django.db.models.fields.DateField')()),
            ('dt_mes_fpos_ini', self.gf('django.db.models.fields.DateField')()),
            ('dt_mes_fpos_fim', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('faturamento', ['CicloFaturamento'])

        # Adding field 'ItemFaturado.nota_fiscal'
        db.add_column('faturamento_itemfaturado', 'nota_fiscal', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['faturamento.NotaFiscal']), keep_default=False)

        # Adding field 'NotaFiscal.lote'
        db.add_column('faturamento_notafiscal', 'lote', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['faturamento.LoteFaturamento']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'DataCalendario'
        db.delete_table('faturamento_datacalendario')

        # Deleting model 'LoteFaturamento'
        db.delete_table('faturamento_lotefaturamento')

        # Deleting model 'Duplicata'
        db.delete_table('faturamento_duplicata')

        # Deleting model 'CicloFaturamentoDefault'
        db.delete_table('faturamento_ciclofaturamentodefault')

        # Deleting model 'CicloFaturamento'
        db.delete_table('faturamento_ciclofaturamento')

        # Deleting field 'ItemFaturado.nota_fiscal'
        db.delete_column('faturamento_itemfaturado', 'nota_fiscal_id')

        # Deleting field 'NotaFiscal.lote'
        db.delete_column('faturamento_notafiscal', 'lote_id')


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
        'faturamento.ciclofaturamento': {
            'Meta': {'object_name': 'CicloFaturamento'},
            'ciclo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['faturamento.CicloFaturamentoDefault']"}),
            'data_faturamento': ('django.db.models.fields.DateField', [], {}),
            'data_vencimento': ('django.db.models.fields.DateField', [], {}),
            'dt_mes_corr_fim': ('django.db.models.fields.DateField', [], {}),
            'dt_mes_corr_ini': ('django.db.models.fields.DateField', [], {}),
            'dt_mes_fpos_fim': ('django.db.models.fields.DateField', [], {}),
            'dt_mes_fpos_ini': ('django.db.models.fields.DateField', [], {}),
            'dt_mes_fpre_fim': ('django.db.models.fields.DateField', [], {}),
            'dt_mes_fpre_ini': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'faturamento.ciclofaturamentodefault': {
            'Meta': {'object_name': 'CicloFaturamentoDefault'},
            'dia_faturamento': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'}),
            'dia_venc_default': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'faturamento.datacalendario': {
            'Meta': {'object_name': 'DataCalendario'},
            'data': ('django.db.models.fields.DateField', [], {'unique': 'True', 'db_index': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'feriado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'faturamento.duplicata': {
            'Meta': {'object_name': 'Duplicata'},
            'data_pagamento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota_fiscal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['faturamento.NotaFiscal']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
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
            'nota_fiscal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['faturamento.NotaFiscal']"}),
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
        'faturamento.lotefaturamento': {
            'Meta': {'object_name': 'LoteFaturamento'},
            'ciclo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['faturamento.CicloFaturamento']", 'null': 'True'}),
            'data_faturamento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tipo_lote': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'faturamento.notafiscal': {
            'Meta': {'object_name': 'NotaFiscal'},
            'data_pagamento': ('django.db.models.fields.DateField', [], {}),
            'endereco_faturamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Endereco']"}),
            'fim_fatura': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio_fatura': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'lote': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['faturamento.LoteFaturamento']"}),
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
