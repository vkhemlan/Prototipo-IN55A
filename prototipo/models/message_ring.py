#-*- coding: UTF-8 -*-
from django.db import models
from message_category import MessageCategory
from group import Group

'''
Descripcion del contexto de una serie de mensajes
asociados a cierto grupo.
Tiene controles de privacidad
'''
class MessageRing(models.Model):
    group = models.ForeignKey(Group)
    category = models.ForeignKey(MessageCategory)
    include_group = models.BooleanField()
    include_assistant_and_auxiliary = models.BooleanField()
    include_coordinator = models.BooleanField()
    title = models.CharField(max_length = 255)

    def __unicode__(self):
        return unicode(self.group) + ' - ' + self.title
    
    class Meta:
        app_label = 'prototipo'
