from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
  context_dict = {}
  return render(request, 'ox_web/index.html', context_dict)

def about(request):
  return HttpResponse("This is the about page.")
