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
