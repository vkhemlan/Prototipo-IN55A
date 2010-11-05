#-*- coding: UTF-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.admin.models import User
from common_role_info import CommonRoleInfo
from prototipo.models import CourseInstance

'''
Descripcion de los auxiliares del curso
'''
class Auxiliary(CommonRoleInfo):
    person = models.ForeignKey(User)
    course_instance = models.ForeignKey(CourseInstance)
    role_name = 'Auxiliar'
    
    def __unicode__(self):
        return unicode(self.course_instance) + ' - ' + self.person.get_full_name()
        
    class Meta:
        app_label = 'prototipo'
        unique_together = (('person', 'course_instance'))
