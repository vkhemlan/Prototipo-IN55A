#-*- coding: UTF-8 -*-
from django import forms
from prototipo.models import *

class StudentMessageRingForm(forms.Form):
    category = forms.ModelChoiceField(queryset = MessageCategory.objects.all(), label = 'Categoria:')
    title = forms.CharField(label = 'Titulo:')
    body = forms.CharField(widget = forms.Textarea, label = 'Cuerpo:')
    include_assistant_and_auxiliary = forms.BooleanField(label = 'Incluir al auxiliar y ayudante?', required = False, initial = True)
    include_coordinator = forms.BooleanField(label = 'Incluir al coordinador?', required = False)

