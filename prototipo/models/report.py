#-*- coding: UTF-8 -*-
from django.db import models
from group import Group
from report_description import ReportDescription

'''
Descripcion de una de las entregas de cierto grupo
y de su feedback asociado
'''
class Report(models.Model):
    description = models.ForeignKey(ReportDescription)
    group = models.ForeignKey(Group)
    blocked = models.BooleanField()
    feedback_key = models.CharField(max_length = 255)
    corrected = models.BooleanField()
    last_delivery_date = models.DateTimeField(blank = True, null = True)
    first_correction_date = models.DateTimeField(blank = True, null = True)
    validation_date = models.DateTimeField(blank = True, null = True)
    
    def __unicode__(self):
        return unicode(self.description) + ' - ' + unicode(self.group)
    
    class Meta:
        app_label = 'prototipo'
