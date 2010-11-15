#-*- coding: UTF-8 -*-
from django import forms
from prototipo.models import *

class ReportDeliveryForm(forms.Form):
    report = forms.FileField(label = 'Entrega (Solo un archivo)')

