# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Auxiliary', fields ['person', 'course_instance']
        db.create_unique('prototipo_auxiliary', ['person_id', 'course_instance_id'])

        # Adding unique constraint on 'Season', fields ['name']
        db.create_unique('prototipo_season', ['name'])

        # Adding unique constraint on 'Assistant', fields ['person', 'course_instance']
        db.create_unique('prototipo_assistant', ['person_id', 'course_instance_id'])

        # Adding unique constraint on 'Student', fields ['person', 'course_instance']
        db.create_unique('prototipo_student', ['person_id', 'course_instance_id'])

        # Adding unique constraint on 'CourseInstance', fields ['season', 'year']
        db.create_unique('prototipo_courseinstance', ['season_id', 'year'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Auxiliary', fields ['person', 'course_instance']
        db.delete_unique('prototipo_auxiliary', ['person_id', 'course_instance_id'])

        # Removing unique constraint on 'Season', fields ['name']
        db.delete_unique('prototipo_season', ['name'])

        # Removing unique constraint on 'Assistant', fields ['person', 'course_instance']
        db.delete_unique('prototipo_assistant', ['person_id', 'course_instance_id'])

        # Removing unique constraint on 'Student', fields ['person', 'course_instance']
        db.delete_unique('prototipo_student', ['person_id', 'course_instance_id'])

        # Removing unique constraint on 'CourseInstance', fields ['season', 'year']
        db.delete_unique('prototipo_courseinstance', ['season_id', 'year'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'prototipo.assistant': {
            'Meta': {'unique_together': "(('person', 'course_instance'),)", 'object_name': 'Assistant'},
            'course_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.CourseInstance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'prototipo.auxiliary': {
            'Meta': {'unique_together': "(('person', 'course_instance'),)", 'object_name': 'Auxiliary'},
            'course_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.CourseInstance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'prototipo.courseinstance': {
            'Meta': {'unique_together': "(('year', 'season'),)", 'object_name': 'CourseInstance'},
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.Season']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'prototipo.group': {
            'Meta': {'object_name': 'Group'},
            'assistant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.Assistant']"}),
            'auxiliary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.Auxiliary']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'led_group'", 'to': "orm['prototipo.Student']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'prototipo.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ring': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.MessageRing']"})
        },
        'prototipo.messagecategory': {
            'Meta': {'object_name': 'MessageCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'prototipo.messagering': {
            'Meta': {'object_name': 'MessageRing'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.MessageCategory']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_assistant_and_auxiliary': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'include_coordinator': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'include_group': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'prototipo.report': {
            'Meta': {'object_name': 'Report'},
            'blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'corrected': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.ReportDescription']"}),
            'feedback_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_correction_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_delivery_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'validation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'prototipo.reportdescription': {
            'Meta': {'object_name': 'ReportDescription'},
            'course_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.CourseInstance']"}),
            'delivery_end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'delivery_start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'feedback_return_date': ('django.db.models.fields.DateTimeField', [], {}),
            'feedback_template_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'prototipo.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {})
        },
        'prototipo.student': {
            'Meta': {'unique_together': "(('person', 'course_instance'),)", 'object_name': 'Student'},
            'course_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.CourseInstance']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['prototipo']
