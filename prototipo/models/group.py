#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.admin.models import User
from django.core.exceptions import ValidationError
from course_instance import CourseInstance
from auxiliary import Auxiliary
from assistant import Assistant

'''
Descripcion de los grupos de trabajo
Cada uno tiene un ayudante y asistente a cargo
ademas de un lider de equipo
'''
class Group(models.Model):
    auxiliary = models.ForeignKey(Auxiliary)
    assistant = models.ForeignKey(Assistant)
    leader = models.ForeignKey('Student', related_name = 'led_group')
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name
    
    def clean(self):
        if not self.auxiliary.course_instance == self.assistant.course_instance == self.leader.course_instance:
            raise ValidationError('El ayudante, auxiliar y líder de equipo deben pertenecer a la misma versión del curso')
            
        if self.leader.group != self:
            raise ValidationError('El líder de grupo debe pertenecer a este equipo')
            
    class Meta:
        app_label = 'prototipo'
