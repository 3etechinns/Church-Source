import sys

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

import django.contrib.auth.models as amodels
from django.contrib.contenttypes.models import ContentType

class Migration(DataMigration):
    depends_on = (
        ("check_in", "0008_auto__add_field_event_link"),
        ("resources", "0001_initial"),
    )
    
    def forwards(self, orm):
        pass
        
    def backwards(self, orm):
        pass
        
    models = {
        'people.address': {
            'Meta': {'ordering': "('address1',)", 'object_name': 'Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'atype': ('django.db.models.fields.CharField', [], {'default': "'ns'", 'max_length': '10'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'household': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Household']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'people.group': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Group'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gtype': ('django.db.models.fields.CharField', [], {'default': "'general'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resources.Room']", 'null': 'True', 'blank': 'True'})
        },
        'people.groupadmin': {
            'Meta': {'ordering': "('group__name', 'person__lname', 'person__fname')", 'object_name': 'GroupAdmin'},
            'can_send': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"})
        },
        'people.household': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Household'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'anniversary': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_visit': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_temp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.TempImage']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'ns'", 'max_length': '10'})
        },
        'people.person': {
            'Meta': {'ordering': "('lname', 'fname')", 'object_name': 'Person'},
            'alerts': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allergies': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'ns'", 'max_length': '10'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.Group']", 'null': 'True', 'blank': 'True'}),
            'household': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Household']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_temp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.TempImage']", 'null': 'True', 'blank': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'mname': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'ns'", 'max_length': '10'})
        },
        'people.phone': {
            'Meta': {'ordering': "('person__lname', 'person__fname', 'number')", 'object_name': 'Phone'},
            'alerts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'type1': ('django.db.models.fields.CharField', [], {'default': "'ns'", 'max_length': '10'}),
            'type2': ('django.db.models.fields.CharField', [], {'default': "'ns'", 'max_length': '10'})
        },
        'people.tempimage': {
            'Meta': {'ordering': "('-ts',)", 'object_name': 'TempImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ts': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'resources.room': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Room'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['people']
