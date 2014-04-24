# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Deck.title'
        db.delete_column(u'djecks_anki_deck', 'title')

        # Deleting field 'Deck.description'
        db.delete_column(u'djecks_anki_deck', 'description')

        # Adding field 'Deck.parent'
        db.add_column(u'djecks_anki_deck', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks.Deck'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Deck.title'
        db.add_column(u'djecks_anki_deck', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Deck.description'
        db.add_column(u'djecks_anki_deck', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Deck.parent'
        db.delete_column(u'djecks_anki_deck', 'parent_id')


    models = {
        u'djecks.deck': {
            'Meta': {'object_name': 'Deck'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'djecks_anki.deck': {
            'Meta': {'object_name': 'Deck'},
            'apkg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks.Deck']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['djecks_anki']