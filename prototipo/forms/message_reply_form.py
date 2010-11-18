#-*- coding: UTF-8 -*-
from django import forms
from prototipo.models import *

class MessageReplyForm(forms.Form):
    body = forms.CharField(widget = forms.Textarea, label = "Respuesta:")

