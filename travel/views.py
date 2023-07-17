from django.shortcuts import render
from travel.models import destination

# Create your views here.
def index(request):
    dests = destination.objects.all()
    return render(request, 'index.html', {'destt': dests})  