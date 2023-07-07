from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
  return HttpResponse('Hello World', {'name' : 'SAGAR'})

def home(request):
  return render(request, 'home.html', {'name' : 'SAGAR'})

def add(request):
  val1 = int(request.POST['num1'])
  val2 = int(request.POST['num2'])
  res = val1 + val2
  return render(request, 'results.html', {'result' : res})