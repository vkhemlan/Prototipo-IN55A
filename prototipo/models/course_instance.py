#-*- coding: UTF-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.admin.models import User
from common_role_info import CommonRoleInfo
from prototipo.models import Season

'''
Descripcion de una instancia particular del curso 
Ejemplo: Primavera 2010
'''
class CourseInstance(CommonRoleInfo):
    year = models.IntegerField()
    season = models.ForeignKey(Season)
    coordinator = models.ForeignKey(User)
    role_name = 'Coordinador'
        
    course_instance = property(lambda self: self)
    
    def get_view_name(self):
        return 'coordinator'
    
    def __unicode__(self):
        return unicode(self.season) + ' ' + str(self.year)
        
    def get_value(self):
        num_seasons = Season.objects.count()
        return self.year + 1.0 * self.season.ordering / num_seasons
    
    class Meta:
        app_label = 'prototipo'
        ordering = ('-year', 'season',)
        unique_together = (('year', 'season'))
