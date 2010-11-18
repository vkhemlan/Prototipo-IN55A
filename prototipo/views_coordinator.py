from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import settings
from forms import *
from models import *
from utils import *
from utils.functions import *

def coordinator_login_required(f):
    def wrap(request, *args, **kwargs):
        coordinator_id = kwargs['coordinator_id']
        course_instance = CourseInstance.objects.get(pk = coordinator_id)
        if course_instance.coordinator == request.user:
            return f(request, course_instance, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
            
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

@coordinator_login_required
def index(request, course_instance, coordinator_id):
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    return render_to_response('coordinator/index.html', {
        'roles': roles,
        'course_instance': course_instance
    })
    
@coordinator_login_required
def report_description(request, course_instance, coordinator_id):
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    reports = ReportDescription.objects.filter(course_instance = course_instance)
    return render_to_response('coordinator/report.html', {
        'roles': roles,
        'course_instance': course_instance,
        'reports': reports,
    })
    
@coordinator_login_required
def add_report_description(request, course_instance, coordinator_id):
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    
    if request.method == 'POST':
        form = ReportDescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            report_description = ReportDescription.generate_report(form, course_instance)
            return HttpResponseRedirect(reverse('prototipo.views_coordinator.report_description', kwargs = {'coordinator_id': coordinator_id}))
    else:
        form = ReportDescriptionForm()
    return render_to_response('coordinator/add_report_description.html', {
        'roles': roles,
        'course_instance': course_instance,
        'report_description_form': form,
    }, context_instance = RequestContext(request))
    
@coordinator_login_required
def message(request, course_instance, coordinator_id):
    groups = Group.objects.filter(leader__course_instance = course_instance)
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    message_rings = []
    for group in groups:
        group_message_rings = MessageRing.objects.filter(group = group).filter(include_coordinator = True)
        message_rings.extend(group_message_rings)
        
    return render_to_response('coordinator/message.html', {
        'course_instance': course_instance,
        'roles': roles,        
        'message_rings': message_rings,
    })

@coordinator_login_required
def message_details(request, course_instance, coordinator_id, message_ring_id):
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    message_ring = MessageRing.objects.get(pk = message_ring_id)
    messages = message_ring.message_set.all().order_by('date')
    
    return render_to_response('coordinator/message_details.html', {
        'course_instance': course_instance,
        'roles': roles,        
        'messages': messages,
        'message_ring': message_ring,
    })

@coordinator_login_required
def message_add(request, course_instance, coordinator_id):
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    
    if request.method == 'POST':
        form = CoordinatorMessageRingForm(request.POST)
        if form.is_valid():
            message_ring = MessageRing()
            message_ring.group = form.cleaned_data['group']
            message_ring.category = form.cleaned_data['category']
            message_ring.include_group = form.cleaned_data['include_group']
            message_ring.include_assistant_and_auxiliary = form.cleaned_data['include_assistant_and_auxiliary']
            message_ring.include_coordinator = True
            message_ring.title = form.cleaned_data['title']
            message_ring.save()
        
            message = Message()
            message.ring = message_ring
            message.body = form.cleaned_data['body']
            message.remitent = request.user
            message.save()
            
            send_notification_mails(message_ring)
            
            return HttpResponseRedirect(reverse('prototipo.views_coordinator.message', kwargs = {'coordinator_id': coordinator_id}))
    else:
        form = CoordinatorMessageRingForm.create_form(course_instance)
        
    return render_to_response('coordinator/message_add.html', {
        'roles': roles,
        'course_instance': course_instance,
        'form': form,
    }, context_instance = RequestContext(request))
    
@coordinator_login_required
def message_reply(request, course_instance, coordinator_id, message_ring_id):
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    
    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            message = Message()
            message.ring = MessageRing.objects.get(pk = message_ring_id)
            message.body = form.cleaned_data['body']
            message.remitent = request.user
            message.save()
            
            send_notification_mails(message.ring)            
            
            return HttpResponseRedirect(reverse('prototipo.views_coordinator.message_details', kwargs = {'coordinator_id': coordinator_id, 'message_ring_id': message_ring_id}))
    else:
        form = MessageReplyForm()
    return render_to_response('coordinator/message_reply.html', {
        'roles': roles,
        'course_instance': course_instance,
        'message_reply_form': form,
    }, context_instance = RequestContext(request))
    
def send_notification_mails(message_ring):
    if message_ring.include_group:
        group = message_ring.group
        for student in group.student_set.all():
            send_new_message_mail(student.person)
    if message_ring.include_assistant_and_auxiliary:
        send_new_message_mail(group.assistant.person)
        send_new_message_mail(group.auxiliary.person)
