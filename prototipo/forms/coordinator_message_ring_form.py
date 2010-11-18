#-*- coding: UTF-8 -*-
from django import forms
from prototipo.models import *

class CoordinatorMessageRingForm(forms.Form):
    group = forms.ModelChoiceField(queryset = Group.objects.all(), label = 'Grupo:')
    category = forms.ModelChoiceField(queryset = MessageCategory.objects.all(), label = 'Categoria:')
    title = forms.CharField(label = 'Titulo:')
    body = forms.CharField(widget = forms.Textarea, label = 'Cuerpo:')
    include_group = forms.BooleanField(label = 'Incluir al grupo?', required = False)
    include_assistant_and_auxiliary = forms.BooleanField(label = 'Incluir al auxiliar y ayudante?', required = False)
    
    @staticmethod
    def create_form(course_instance):
        form = CoordinatorMessageRingForm()
        form.fields['group'].queryset = Group.objects.filter(leader__course_instance = course_instance)
        return form

