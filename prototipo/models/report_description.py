#-*- coding: UTF-8 -*-
from django.db import models
from course_instance import CourseInstance

'''
Esquema de una entrega, define fechas y el 
template a ocupar para su feedback
'''
class ReportDescription(models.Model):
    name = models.CharField(max_length = 255)
    course_instance = models.ForeignKey(CourseInstance)
    delivery_start_date = models.DateTimeField()
    delivery_end_date = models.DateTimeField()
    feedback_return_date = models.DateTimeField()
    feedback_template_key = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return unicode(self.course_instance) + ' - ' + self.name
    
    class Meta:
        app_label = 'prototipo'
