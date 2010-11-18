from datetime import datetime
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import settings
from forms import *
from models import *
from utils import *

def assistant_login_required(f):
    def wrap(request, *args, **kwargs):
        assistant_id = kwargs['assistant_id']
        assistant = Assistant.objects.get(pk = assistant_id)
        del kwargs['assistant_id']
        if assistant.person == request.user:
            return f(request, assistant, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
            
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

@assistant_login_required
def index(request, assistant):
    roles = RoleList(request.user)
    roles.set_default(Assistant, assistant.id)
    return render_to_response('assistant/index.html', {
        'roles': roles,
        'assistant': assistant
    })
    
@assistant_login_required
def report(request, assistant):
    roles = RoleList(request.user)
    roles.set_default(Assistant, assistant.id)
    report_descriptions = ReportDescription.objects.all()
    for report_description in report_descriptions:
        report_description.reports = Report.objects.filter(description = report_description).filter(group__assistant = assistant)
    return render_to_response('assistant/report.html', {
        'roles': roles,
        'assistant': assistant,
        'report_descriptions': report_descriptions,
    })
    
@assistant_login_required
def mark_as_corrected(request, assistant, report_id):
    report = Report.objects.get(pk = report_id)
    if report.group.assistant != assistant:
        raise Exception
    if not report.first_correction_date:
        report.first_correction_date = datetime.now()
    report.corrected = True
    report.save()
    url = reverse('prototipo.views_assistant.report', kwargs = {'assistant_id': assistant.id})
    return HttpResponseRedirect(url)
    
@assistant_login_required
def message(request, assistant):
    roles = RoleList(request.user)
    roles.set_default(Assistant, assistant.id)
    message_rings = []
    for group in assistant.group_set.all():
        group_message_rings = MessageRing.objects.filter(group = group).filter(include_assistant_and_auxiliary = True)
        message_rings.extend(group_message_rings)
        
    return render_to_response('assistant/message.html', {
        'assistant': assistant,
        'roles': roles,        
        'message_rings': message_rings,
    })
@assistant_login_required
def message_details(request, assistant, message_ring_id):
    roles = RoleList(request.user)
    roles.set_default(Assistant, assistant.id)
    message_ring = MessageRing.objects.get(pk = message_ring_id)
    messages = message_ring.message_set.all().order_by('date')
    
    return render_to_response('assistant/message_details.html', {
        'assistant': assistant,
        'roles': roles,        
        'messages': messages,
        'message_ring': message_ring,
    })

@assistant_login_required
def message_add(request, assistant):
    roles = RoleList(request.user)
    roles.set_default(Assistant, assistant.id)
    
    if request.method == 'POST':
        form = AssistantAuxiliaryMessageRingForm(request.POST)
        if form.is_valid():
            message_ring = MessageRing()
            message_ring.group = form.cleaned_data['group']
            message_ring.category = form.cleaned_data['category']
            message_ring.include_coordinator = form.cleaned_data['include_coordinator']
            message_ring.include_assistant_and_auxiliary = True
            message_ring.include_group = form.cleaned_data['include_group']
            message_ring.title = form.cleaned_data['title']
            message_ring.save()
        
            message = Message()
            message.ring = message_ring
            message.body = form.cleaned_data['body']
            message.remitent = request.user
            message.save()
            return HttpResponseRedirect(reverse('prototipo.views_assistant.message', kwargs = {'assistant_id': assistant.id}))
    else:
        form = AssistantAuxiliaryMessageRingForm.create_form(assistant)
        
    return render_to_response('assistant/message_add.html', {
        'roles': roles,
        'assistant': assistant,
        'form': form,
    }, context_instance = RequestContext(request))
    
@assistant_login_required
def message_reply(request, assistant, message_ring_id):
    roles = RoleList(request.user)
    roles.set_default(Assistant, assistant.id)
    
    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            message = Message()
            message.ring = MessageRing.objects.get(pk = message_ring_id)
            message.body = form.cleaned_data['body']
            message.remitent = request.user
            message.save()
            return HttpResponseRedirect(reverse('prototipo.views_assistant.message_details', kwargs = {'assistant_id': assistant.id, 'message_ring_id': message_ring_id}))
    else:
        form = MessageReplyForm()
    return render_to_response('assistant/message_reply.html', {
        'roles': roles,
        'assistant': assistant,
        'message_reply_form': form,
    }, context_instance = RequestContext(request))
