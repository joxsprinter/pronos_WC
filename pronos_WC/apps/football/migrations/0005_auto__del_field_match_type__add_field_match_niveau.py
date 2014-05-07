# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Match.type'
        db.delete_column(u'football_match', 'type')

        # Adding field 'Match.niveau'
        db.add_column(u'football_match', 'niveau',
                      self.gf('django.db.models.fields.CharField')(default=u'atch de poule', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Match.type'
        db.add_column(u'football_match', 'type',
                      self.gf('django.db.models.fields.CharField')(default=u'atch de poule', max_length=20),
                      keep_default=False)

        # Deleting field 'Match.niveau'
        db.delete_column(u'football_match', 'niveau')


    models = {
        u'football.equipe': {
            'Meta': {'ordering': "[u'poule', u'nom']", 'object_name': 'Equipe'},
            'drapeau': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'poule': ('django.db.models.fields.CharField', [], {'default': "u'A'", 'max_length': '1'})
        },
        u'football.joueur': {
            'Meta': {'object_name': 'Joueur'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'football.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'equipe1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'equipe1_content_type'", 'to': u"orm['football.Equipe']"}),
            'equipe1_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equipe2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'equipe2_content_type'", 'to': u"orm['football.Equipe']"}),
            'equipe2_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'niveau': ('django.db.models.fields.CharField', [], {'default': "u'atch de poule'", 'max_length': '20'}),
            'traite': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'football.pronostic': {
            'Meta': {'unique_together': "((u'joueur', u'match'),)", 'object_name': 'Pronostic'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'equipe1_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equipe2_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joueur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Joueur']"}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Match']"})
        }
    }

    complete_apps = ['football']