from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from itsense import settings
from forms import *
from models import *

def login(request):
    next_url = '/'
    if 'next' in request.GET:
        next_url = request.GET['next']

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username = username, password = password)

            if user:
                auth.login(request, user)
    else:
        form = LoginForm()

    if request.user.is_authenticated():
        return HttpResponseRedirect(next_url)
    else:
        return render_to_response('login.html',{
            'login_form': form
        }, context_instance = RequestContext(request))
        
@login_required
def logout(request):
    auth.logout(request)
    next_url = '/'
    if 'next' in request.GET:
        next_url = request.GET['next']
    return HttpResponseRedirect(next_url)
            
@login_required
def index(request):
    user = request.user
    coordinator_roles = user.courseinstance_set.all()
    auxiliary_roles = user.auxiliary_set.all()
    assistant_roles = user.assistant_set.all()
    student_roles = user.student_set.all()

    return render_to_response('index.html', {
        'user': user,
        'coordinator_roles': coordinator_roles,
        'auxiliary_roles': auxiliary_roles,
        'assistant_roles': assistant_roles,
        'student_roles': student_roles,
    })
