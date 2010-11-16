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
