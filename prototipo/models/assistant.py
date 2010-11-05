#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.admin.models import User
from course_instance import CourseInstance

'''
Descripcion de los ayudantes del curso
'''
class Assistant(models.Model):
    person = models.ForeignKey(User)
    course_instance = models.ForeignKey(CourseInstance)
    
    def __unicode__(self):
        return unicode(self.course_instance) + ' - ' + self.person.get_full_name()
    
    class Meta:
        app_label = 'prototipo'
        unique_together = (('person', 'course_instance'))
