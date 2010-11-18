#-*- coding: UTF-8 -*-
from django import forms
from prototipo.models import *

class AssistantAuxiliaryMessageRingForm(forms.Form):
    group = forms.ModelChoiceField(queryset = Group.objects.all(), label = 'Grupo:')
    category = forms.ModelChoiceField(queryset = MessageCategory.objects.all(), label = 'Categoria:')
    title = forms.CharField(label = 'Titulo:')
    body = forms.CharField(widget = forms.Textarea, label = 'Cuerpo:')
    include_coordinator = forms.BooleanField(label = 'Incluir al coordinador?', required = False)
    include_group = forms.BooleanField(label = 'Incluir al grupo?', required = False, initial = True)
    
    @staticmethod
    def create_form(assistant_auxiliary):
        form = AssistantAuxiliaryMessageRingForm()
        form.fields['group'].queryset = Group.objects.filter(leader__course_instance = assistant_auxiliary.course_instance)
        return form

