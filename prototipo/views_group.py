from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
import settings
from forms import *
from models import *
from utils import *

def group_login_required(f):
    def wrap(request, *args, **kwargs):
        group_id = kwargs['group_id']
        del kwargs['group_id']
        group = Group.objects.get(pk = group_id)
        users = [s.person for s in group.student_set.all()]
        if request.user in users:
            return f(request, group, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
            
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

@group_login_required
def index(request, group):
    roles = RoleList(request.user)
    student = Student.objects.filter(group = group).filter(person = request.user)[0]
    roles.set_default(Student, student.id)
    return render_to_response('group/index.html', {
        'roles': roles,
        'group': group
    })
    
@group_login_required
def report(request, group):
    roles = RoleList(request.user)
    student = Student.objects.filter(group = group).filter(person = request.user)[0]
    roles.set_default(Student, student.id)
    now = datetime.now()
    reports = Report.objects.filter(description__delivery_start_date__lte = now).filter(group = group)
    past_reports = reports.filter(description__delivery_end_date__lte = now)
    current_reports = reports.filter(description__delivery_end_date__gt = now)
    return render_to_response('group/report.html', {
        'roles': roles,
        'group': group,
        'past_reports': past_reports,
        'current_reports': current_reports,
    })

@group_login_required
def deliver_report(request, group, report_id):
    roles = RoleList(request.user)
    student = Student.objects.filter(group = group).filter(person = request.user)[0]
    roles.set_default(Student, student.id)

    try:
        report = Report.objects.get(pk = report_id)
        if report.group != group:
            raise Exception

        if report.description.delivery_end_date < datetime.now():
            raise Exception
    except:
        return HttpResponseRedirect('/')
    
    if request.method == 'POST':
        form = ReportDeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            report.store_file(form.cleaned_data['report'])
            report.last_delivery_date = datetime.now()
            report.save()
            return HttpResponseRedirect(reverse('prototipo.views_group.report', kwargs = {'group_id': group.id}))
    else:
        form = ReportDeliveryForm()
    return render_to_response('group/report_delivery.html', {
        'roles': roles,
        'group': group,
        'report_delivery_form': form,
    }, context_instance = RequestContext(request))