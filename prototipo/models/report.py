#-*- coding: UTF-8 -*-
from django.db import models
from group import Group
from prototipo.utils.functions import get_file_extension, upload_file, get_gdoc_key
import gdata.docs.service
import gdata.docs.data
import gdata.docs.client
import gdata.spreadsheet.service
import settings

'''
Descripcion de una de las entregas de cierto grupo
y de su feedback asociado
'''
class Report(models.Model):
    description = models.ForeignKey('ReportDescription')
    group = models.ForeignKey(Group)
    blocked = models.BooleanField()
    feedback_key = models.CharField(max_length = 255)
    corrected = models.BooleanField()
    last_delivery_date = models.DateTimeField(blank = True, null = True)
    first_correction_date = models.DateTimeField(blank = True, null = True)
    validation_date = models.DateTimeField(blank = True, null = True)
    
    @staticmethod
    def generate_report(report_description, group):
        report = Report()
        report.description = report_description
        report.group = group
        report.blocked = True
        report.corrected = False
        
        document_url = upload_file(report.description, str(report.description.course_instance) + ' - ' + report.description.name + ' - ' + report.group.name)
        report.feedback_key = get_gdoc_key(document_url)
        report.share_with_assistant()
        report.share_with_auxiliary()
        report.save()
        
    def share_with_assistant(self):
        self.share('writer', self.group.assistant.person.email)
        
    def share_with_auxiliary(self):
        self.share('reader', self.group.auxiliary.person.email)
        
    def share(self, permissions, email):
        gd_client = gdata.docs.service.DocsService()
        gd_client.ClientLogin(settings.ACCOUNT_EMAIL, settings.ACCOUNT_PASSWORD)
        feed_url = 'https://docs.google.com/feeds/acl/private/full/spreadsheet%3A' + self.feedback_key
        
        scope = gdata.docs.Scope(value = email, type = 'user')
        role = gdata.docs.Role(value = permissions)
        acl_entry = gdata.docs.DocumentListAclEntry(scope = scope, role = role)

        created_acl_entry = gd_client.Post(acl_entry, feed_url, converter = gdata.docs.DocumentListAclEntryFromString)
        
        
    def __unicode__(self):
        return unicode(self.description) + ' - ' + unicode(self.group)
    
    class Meta:
        app_label = 'prototipo'
