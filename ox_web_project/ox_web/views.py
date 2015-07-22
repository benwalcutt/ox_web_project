from ox_web.forms import UserForm, UserProfileForm, BlogPost
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from ox_web.models import Blog
import os

DATA_PATH = os.path.dirname(os.path.dirname(__file__))

# Create your views here.

def test(request):
  print BASE_DIR
  return HttpResponseRedirect('/ox_web/')

@login_required
def add_post(request):
  if request.method == 'POST':
    post_form = BlogPost(data=request.POST)

    if post_form.is_valid():
      post = post_form.save()
      post.save()

    else:
      print post_form.errors
  else:
    post_form = BlogPost()

  return render(request, 'ox_web/add_post.html', {'post_form': post_form})
    

def register(request):
  registered = False;

  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileForm(data=request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      profile = profile_form.save(commit=False)
      profile.user = user

      profile.save()
      os.mkdir(DATA_PATH + '/data/' + user.username)
      registered = True
    else:
      print user_form.errors, profile_form.errors

  else:
    user_form = UserForm()
    profile_form = UserProfileForm()

  return render(request, 'ox_web/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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
  blog_list = Blog.objects.order_by('-posted')[:10]
  context_dict = {'blog_list': blog_list}
  return render(request, 'ox_web/index.html', context_dict)

def about(request):
  return HttpResponse("This is the about page.")
