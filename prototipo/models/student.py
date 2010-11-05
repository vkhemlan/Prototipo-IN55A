#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.admin.models import User
from django.core.exceptions import ValidationError
from course_instance import CourseInstance
from group import Group

'''
Descripcion de un estudiante en cierta
instancia del curso
'''
class Student(models.Model):
    person = models.ForeignKey(User)
    course_instance = models.ForeignKey(CourseInstance)
    group = models.ForeignKey(Group, blank = True, null = True)

    def __unicode__(self):
        return unicode(self.course_instance) + ' - ' + self.person.get_full_name()    
        
    def clean(self):
        if self.group:
            students = self.group.student_set.all()
            for student in students:
                if self.course_instance != student.course_instance:
                    raise ValidationError('Los integrantes de un grupo deben pertenecer a la misma instancia del curso')
        else:
            if self.led_group.all():
                raise ValidationError('No se puede disociar al estudiante del grupo pues es el jefe de dicho equipo')
                    
                    
    class Meta:
        app_label = 'prototipo'
        unique_together = (('person', 'course_instance'))
