from ox_web.forms import UserForm, UserProfileForm, BlogPost, InputForm, JobForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from ox_web.models import Blog, Job
from django.utils import timezone
import os, subprocess
import oxutils

DATA_PATH = os.path.dirname(os.path.dirname(__file__))

# Create your views here.

@login_required
def view_job(request, username, job_id):
  job = Job.objects.get(id=job_id)
#  job.viewed_at = timezone.now()
  context_dict = {'username': username, 'job': job}
  return render(request, 'ox_web/view_job.html', context_dict)

@login_required
def execute(request, username, job_id):
  job = Job.objects.get(id=job_id)
  job.executed_at = timezone.now()
  job.save()
  CMD = ['/home/ben/Documents/oxDNA_gold/branches/oxDNA_v2.2_branch/oxDNA/build/bin/oxDNA', DATA_PATH + '/data/' + request.user.username + '/' + job_id + '/inputMD']
  subprocess.Popen(CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  return HttpResponseRedirect('/ox_web/' + username + '/jobs/')

@login_required
def new_job(request):
  if request.method == 'POST':
    in_form = InputForm(data=request.POST)
    JOB_PATH = DATA_PATH + '/data/' + request.user.username
    job = Job(author=request.user.username, created_at=timezone.now(), data_path=JOB_PATH, active=True)
    job.save()
    job.output_path = JOB_PATH + '/' + str(job.id)
    job.executed_at = None
    job.save()
    NEW_PATH = DATA_PATH + '/data/' + request.user.username + '/' + str(job.id)
    os.mkdir(NEW_PATH)

    if in_form.is_valid():
      inputfile = in_form.cleaned_data
      inputfile['topology'] = NEW_PATH + '/generated.top'
      inputfile['conf_file'] = NEW_PATH + '/generated.dat'
      inputfile['last_conf_file'] = NEW_PATH + '/last_conf.dat'
      inputfile['trajectory_file'] = NEW_PATH + '/trajectory.dat'
      inputfile['log_file'] = NEW_PATH + '/log_file.log'
      inputfile['energy_file'] = NEW_PATH + '/energy.dat'
      oxutils.test(inputfile, request.user.username, job.id)      
    else:
      print in_form.errors
    
    return HttpResponseRedirect('/ox_web/'+request.user.username+'/jobs/')
  else:
    in_form = InputForm()
    context_dict = {'username': request.user.username, 'in_form': in_form}
  return render(request, 'ox_web/new_job.html', context_dict)


def test(request):
  oxutils.test(None, 'ben', 16)
  return HttpResponseRedirect('/ox_web/')

@login_required
def add_post(request, username):
  if request.method == 'POST':
    post_form = BlogPost(data=request.POST)

    if post_form.is_valid():
      post = post_form.save()
      post.author = username
      post.save()

    else:
      print post_form.errors

    return HttpResponseRedirect('/ox_web/')
  else:
    post_form = BlogPost()

  return render(request, 'ox_web/add_post.html', {'post_form': post_form, 'username': username})
    
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

@login_required
def jobs(request, username):
  jobs = Job.objects.all().filter(author=username, active=True).order_by('-id')
  context_dict = {'jobs': jobs, 'username': username}
  return render(request, 'ox_web/jobs.html', context_dict)

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
