#-*- coding: UTF-8 -*-
from django import forms
from prototipo.models import *

class ReportDescriptionForm(forms.Form):
    name = forms.CharField(label = 'Nombre de la entrega', max_length = 255)
    delivery_start_date = forms.DateTimeField(label = 'Fecha de inicio de entregas',
        input_formats=('%m/%d/%Y %H:%M'))
    delivery_end_date = forms.DateTimeField(label = 'Fecha de fin de entregas')
    feedback_return_date = forms.DateTimeField(label = 'Fecha de retorno de feedback')
