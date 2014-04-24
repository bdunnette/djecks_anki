# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Deck'
        db.delete_table(u'djecks_anki_deck')

        # Adding model 'AnkiDeck'
        db.create_table(u'djecks_anki_ankideck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deck', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks.Deck'], null=True, blank=True)),
            ('apkg', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'djecks_anki', ['AnkiDeck'])


    def backwards(self, orm):
        # Adding model 'Deck'
        db.create_table(u'djecks_anki_deck', (
            ('apkg', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks.Deck'], null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'djecks_anki', ['Deck'])

        # Deleting model 'AnkiDeck'
        db.delete_table(u'djecks_anki_ankideck')


    models = {
        u'djecks.deck': {
            'Meta': {'object_name': 'Deck'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'djecks_anki.ankideck': {
            'Meta': {'object_name': 'AnkiDeck'},
            'apkg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'deck': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks.Deck']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['djecks_anki']