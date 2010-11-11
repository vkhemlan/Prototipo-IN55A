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
    
    roles = RoleList(request.user)
    
    if roles.is_empty():
        return render_to_response('index.html', {
            'user': user,
        })
        
    return HttpResponseRedirect(roles.get(0).generate_url())

@login_required
def coordinator(request, coordinator_id):
    roles = RoleList(request.user)
    roles.set_default(CourseInstance, coordinator_id)
    return render_to_response('coordinator.html', {'roles': roles})
    
@login_required
def assistant(request, assistant_id):
    roles = RoleList(request.user)
    roles.set_default(Assistant, assistant_id)
    return render_to_response('assistant.html', {'roles': roles})
    
@login_required
def auxiliary(request, auxiliary_id):
    roles = RoleList(request.user)
    roles.set_default(Auxiliary, auxiliary_id)
    return render_to_response('auxiliary.html', {'roles': roles})
    
@login_required
def student(request, student_id):
    roles = RoleList(request.user)
    roles.set_default(Student, student_id)
    return render_to_response('student.html', {'roles': roles})
    
def append_roles_to_response(request, template, args):
    if 'roles' not in args:
        args['roles'] = get_user_roles(request.user)
        
    return render_to_response(template, args)
