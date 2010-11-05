#-*- coding: UTF-8 -*-
from django.db import models

'''
Descripcion de una de las estaciones
en que se da el ramo.
Ejemplo: Primavera, Otono
'''
class Season(models.Model):
    name = models.CharField(max_length = 20, unique = True)
    ordering = models.IntegerField()

    def __unicode__(self):
        return unicode(self.name)
    
    class Meta:
        app_label = 'prototipo'
        ordering = ('-ordering',)
