# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MessageRing'
        db.create_table('prototipo_messagering', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.Group'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.MessageCategory'])),
            ('include_group', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('include_assistant_and_auxiliary', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('include_coordinator', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('prototipo', ['MessageRing'])

        # Adding model 'Auxiliary'
        db.create_table('prototipo_auxiliary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('course_instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.CourseInstance'])),
        ))
        db.send_create_signal('prototipo', ['Auxiliary'])

        # Adding model 'Group'
        db.create_table('prototipo_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('auxiliary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.Auxiliary'])),
            ('assistant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.Assistant'])),
            ('leader', self.gf('django.db.models.fields.related.ForeignKey')(related_name='led_group', to=orm['prototipo.Student'])),
        ))
        db.send_create_signal('prototipo', ['Group'])

        # Adding model 'MessageCategory'
        db.create_table('prototipo_messagecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('prototipo', ['MessageCategory'])

        # Adding model 'Season'
        db.create_table('prototipo_season', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('prototipo', ['Season'])

        # Adding model 'Message'
        db.create_table('prototipo_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ring', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.MessageRing'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('prototipo', ['Message'])

        # Adding model 'Report'
        db.create_table('prototipo_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.ReportDescription'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.Group'])),
            ('blocked', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('feedback_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('corrected', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('last_delivery_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('first_correction_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('validation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('prototipo', ['Report'])

        # Adding model 'Assistant'
        db.create_table('prototipo_assistant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('course_instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.CourseInstance'])),
        ))
        db.send_create_signal('prototipo', ['Assistant'])

        # Adding model 'Student'
        db.create_table('prototipo_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('course_instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.CourseInstance'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.Group'])),
        ))
        db.send_create_signal('prototipo', ['Student'])

        # Adding model 'CourseInstance'
        db.create_table('prototipo_courseinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.Season'])),
            ('coordinator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('prototipo', ['CourseInstance'])

        # Adding model 'ReportDescription'
        db.create_table('prototipo_reportdescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prototipo.CourseInstance'])),
            ('delivery_start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('delivery_end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('feedback_return_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('feedback_template_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('prototipo', ['ReportDescription'])


    def backwards(self, orm):
        
        # Deleting model 'MessageRing'
        db.delete_table('prototipo_messagering')

        # Deleting model 'Auxiliary'
        db.delete_table('prototipo_auxiliary')

        # Deleting model 'Group'
        db.delete_table('prototipo_group')

        # Deleting model 'MessageCategory'
        db.delete_table('prototipo_messagecategory')

        # Deleting model 'Season'
        db.delete_table('prototipo_season')

        # Deleting model 'Message'
        db.delete_table('prototipo_message')

        # Deleting model 'Report'
        db.delete_table('prototipo_report')

        # Deleting model 'Assistant'
        db.delete_table('prototipo_assistant')

        # Deleting model 'Student'
        db.delete_table('prototipo_student')

        # Deleting model 'CourseInstance'
        db.delete_table('prototipo_courseinstance')

        # Deleting model 'ReportDescription'
        db.delete_table('prototipo_reportdescription')


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
            'Meta': {'object_name': 'Assistant'},
            'course_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.CourseInstance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'prototipo.auxiliary': {
            'Meta': {'object_name': 'Auxiliary'},
            'course_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.CourseInstance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'prototipo.courseinstance': {
            'Meta': {'object_name': 'CourseInstance'},
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
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'led_group'", 'to': "orm['prototipo.Student']"})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'prototipo.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'prototipo.student': {
            'Meta': {'object_name': 'Student'},
            'course_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.CourseInstance']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prototipo.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['prototipo']
