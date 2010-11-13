#-*- coding: UTF-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

'''
Métodos genéricos comunes para ayudantes, auxiliares, coordinador y estudiantes
'''
class CommonRoleInfo(models.Model):
    def get_view_name(self):
        return self.__class__.__name__.lower()

    def generate_url(self):
        view = self.get_view_name()
        return reverse('prototipo.views_' + view + '.index', kwargs = {view + '_id': self.id})
        
    def get_select_text(self):
        return unicode(self.course_instance) + ' - ' + self.role_name
    
    class Meta:
        abstract = True
        app_label = 'prototipo'
        
