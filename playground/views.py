from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
  return HttpResponse('Hello World', {'name' : 'SAGAR'})

def home(request):
  return render(request, 'home.html', {'name' : 'SAGAR'})