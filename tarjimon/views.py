from django.shortcuts import render
from django.http import HttpResponse

from .models import Lugat


def index(request):
    soz = request.GET.get('text', None)
    if soz and soz != '':
        natija = Lugat.objects.filter(ingilizcha__contains=soz) | Lugat.objects.filter(uzbekcha__contains=soz)
        natija = natija.all()[:3]
    else:
        natija = None
     

    return render(request, 'index.html', {'q': soz, 'natija': natija})




def salom2(request):
    return HttpResponse('Mening sahifam')

# Create your views here.
