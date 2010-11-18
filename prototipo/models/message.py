#-*- coding: UTF-8 -*-
from django.db import models
from message_ring import MessageRing
from django.contrib.auth.models import User

'''
Uno de los mensajes en el contexto de un anillo
'''
class Message(models.Model):
    ring = models.ForeignKey(MessageRing)
    date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    remitent = models.ForeignKey(User)
    
    def __unicode__(self):
        return unicode(self.ring) + ' #' + str(self.id)
    
    class Meta:
        app_label = 'prototipo'
