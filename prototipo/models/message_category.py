#-*- coding: UTF-8 -*-
from django.db import models

'''
Categoria de los mensajes
'''
class MessageCategory(models.Model):
    name = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = 'prototipo'
