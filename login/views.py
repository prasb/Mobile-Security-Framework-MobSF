from django.shortcuts import render

from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login

 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register_login.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 

def home(request):
    return render_to_response(
    'home_login.html',
    { 'user': request.user }
    )


def getformdetails(request):
    username = request.POST['username']
    password = request.POST['password']
    
    print username
    print password
    
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print "user is logged"    
    return render_to_response(
     'home_login.html',
    { 'user': request.user }
    )   

# Create your views here.
