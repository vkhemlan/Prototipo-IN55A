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

def auxiliary_login_required(f):
    def wrap(request, *args, **kwargs):
        auxiliary_id = kwargs['auxiliary_id']
        auxiliary = Auxiliary.objects.get(pk = auxiliary_id)
        del kwargs['auxiliary_id']
        if auxiliary.person == request.user:
            return f(request, auxiliary, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
            
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

@auxiliary_login_required
def index(request, auxiliary):
    roles = RoleList(request.user)
    roles.set_default(Auxiliary, auxiliary.id)
    return render_to_response('auxiliary/index.html', {
        'roles': roles,
        'auxiliary': auxiliary
    })
    
@auxiliary_login_required
def report(request, auxiliary):
    roles = RoleList(request.user)
    roles.set_default(Auxiliary, auxiliary.id)
    report_descriptions = ReportDescription.objects.all()
    for report_description in report_descriptions:
        report_description.reports = Report.objects.filter(description = report_description).filter(group__auxiliary = auxiliary)
    return render_to_response('auxiliary/report.html', {
        'roles': roles,
        'auxiliary': auxiliary,
        'report_descriptions': report_descriptions,
    })
    
@auxiliary_login_required
def unmark_as_corrected(request, auxiliary, report_id):
    report = Report.objects.get(pk = report_id)
    if report.group.auxiliary != auxiliary:
        return HttpResponseRedirect('/')
    report.corrected = False
    report.save()
    url = reverse('prototipo.views_auxiliary.report', kwargs = {'auxiliary_id': auxiliary.id})
    return HttpResponseRedirect(url)
    
@auxiliary_login_required
def mark_as_validated(request, auxiliary, report_id):
    report = Report.objects.get(pk = report_id)
    if report.group.auxiliary != auxiliary:
        return HttpResponseRedirect('/')
    if not report.corrected:
        return HttpResponseRedirect('/')
    report.validation_date = datetime.now()
    report.save()
    url = reverse('prototipo.views_auxiliary.report', kwargs = {'auxiliary_id': auxiliary.id})
    return HttpResponseRedirect(url)
    
@auxiliary_login_required
def message(request, auxiliary):
    roles = RoleList(request.user)
    roles.set_default(Auxiliary, auxiliary.id)
    message_rings = []
    for group in auxiliary.group_set.all():
        group_message_rings = MessageRing.objects.filter(group = group).filter(include_assistant_and_auxiliary = True)
        message_rings.extend(group_message_rings)
        
    return render_to_response('auxiliary/message.html', {
        'auxiliary': auxiliary,
        'roles': roles,        
        'message_rings': message_rings,
    })
@auxiliary_login_required
def message_details(request, auxiliary, message_ring_id):
    roles = RoleList(request.user)
    roles.set_default(Auxiliary, auxiliary.id)
    message_ring = MessageRing.objects.get(pk = message_ring_id)
    messages = message_ring.message_set.all().order_by('date')
    
    return render_to_response('auxiliary/message_details.html', {
        'auxiliary': auxiliary,
        'roles': roles,        
        'messages': messages,
        'message_ring': message_ring,
    })

@auxiliary_login_required
def message_add(request, auxiliary):
    roles = RoleList(request.user)
    roles.set_default(Auxiliary, auxiliary.id)
    
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
            return HttpResponseRedirect(reverse('prototipo.views_auxiliary.message', kwargs = {'auxiliary_id': auxiliary.id}))
    else:
        form = AssistantAuxiliaryMessageRingForm.create_form(auxiliary)
        
    return render_to_response('auxiliary/message_add.html', {
        'roles': roles,
        'auxiliary': auxiliary,
        'form': form,
    }, context_instance = RequestContext(request))
    
@auxiliary_login_required
def message_reply(request, auxiliary, message_ring_id):
    roles = RoleList(request.user)
    roles.set_default(Auxiliary, auxiliary.id)
    
    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            message = Message()
            message.ring = MessageRing.objects.get(pk = message_ring_id)
            message.body = form.cleaned_data['body']
            message.remitent = request.user
            message.save()
            return HttpResponseRedirect(reverse('prototipo.views_auxiliary.message_details', kwargs = {'auxiliary_id': auxiliary.id, 'message_ring_id': message_ring_id}))
    else:
        form = MessageReplyForm()
    return render_to_response('auxiliary/message_reply.html', {
        'roles': roles,
        'auxiliary': auxiliary,
        'message_reply_form': form,
    }, context_instance = RequestContext(request))
