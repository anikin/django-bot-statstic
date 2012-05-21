# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LogItem'
        db.create_table('bot_statistic_logitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bot', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('log_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('bot_statistic', ['LogItem'])


    def backwards(self, orm):
        
        # Deleting model 'LogItem'
        db.delete_table('bot_statistic_logitem')


    models = {
        'bot_statistic.logitem': {
            'Meta': {'ordering': "['-log_date']", 'object_name': 'LogItem'},
            'bot': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_date': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bot_statistic']
