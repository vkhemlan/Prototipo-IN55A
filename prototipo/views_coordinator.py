from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from itsense import settings
from forms import *
from models import *
from utils import *

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
        form = ReportDescriptionForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ReportDescriptionForm()
    return render_to_response('coordinator/add_report_description.html', {
        'roles': roles,
        'course_instance': course_instance,
        'report_description_form': form,
    }, context_instance = RequestContext(request))
