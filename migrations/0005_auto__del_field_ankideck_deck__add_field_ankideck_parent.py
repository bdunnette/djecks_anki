# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AnkiDeck.deck'
        db.delete_column(u'djecks_anki_ankideck', 'deck_id')

        # Adding field 'AnkiDeck.parent'
        db.add_column(u'djecks_anki_ankideck', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks.Deck'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'AnkiDeck.deck'
        db.add_column(u'djecks_anki_ankideck', 'deck',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks.Deck'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'AnkiDeck.parent'
        db.delete_column(u'djecks_anki_ankideck', 'parent_id')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks.Deck']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['djecks_anki']