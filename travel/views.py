from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    dest1 = destination()
    dest1.name = 'THAIIIIIIILAND'
    dest1.sale = 9
    dest1.img = 'destination-2.jpg'
    dest1.offer = True

    dest2 = destination()
    dest2.name = 'AMWERICAAA'
    dest2.sale = 2
    dest2.img = 'destination-1.jpg'
    dest2.offer = False
    
    dest3 = destination
    dest3.name = 'TAMANG CORPO HQ'
    dest3.sale = 0
    dest3.img = 'destination-3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'destt': dests})