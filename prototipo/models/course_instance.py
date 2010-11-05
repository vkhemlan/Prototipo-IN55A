#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.admin.models import User
from season import Season

'''
Descripcion de una instancia particular del curso 
Ejemplo: Primavera 2010
'''
class CourseInstance(models.Model):
    year = models.IntegerField()
    season = models.ForeignKey(Season)
    coordinator = models.ForeignKey(User)
    
    def __unicode__(self):
        return unicode(self.season) + ' ' + str(self.year)
    
    class Meta:
        app_label = 'prototipo'
        ordering = ('-year', 'season',)
        unique_together = (('year', 'season'))
