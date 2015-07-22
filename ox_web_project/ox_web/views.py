from ox_web.forms import UserForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def jobs(request, username):
  print username
  return render(request, 'ox_web/jobs.html', {})

def contact(request):
  return render(request, 'ox_web/contact.html', {})

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/ox_web/')

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    
    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect('/ox_web/')
      else:
        return HttpResponse('Your account has been disabled. <a href="/ox_web/">Home</a>')

    else:
      print "Invalid login details: {0), {1)".format(username, password)
      return HttpResponse('Invalid login details supplied. <a href="/ox_web/">Home</a>')

  else:
    return render(request, 'ox_web/login.html', {})

def index(request):
  context_dict = {}
  return render(request, 'ox_web/index.html', context_dict)

def about(request):
  return HttpResponse("This is the about page.")
