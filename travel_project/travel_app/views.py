from django.shortcuts import render
from .models import place
from .models import journey


# Create your views here.

def demo(req):
    pls = place.objects.all()
    jrn = journey.objects.all()
    return render(req, 'index.html', {'place': pls, 'journey': jrn})

