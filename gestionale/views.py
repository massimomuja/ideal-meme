import datetime
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from gestionale.models import Esame


def index(request):
    esame = Esame()

    esame.data = datetime.datetime.now()
    esame.tipo = 'test'
    esame.esito = 'esito2'
    esame.struttura = 'struttura3'
    esame.save() #inesrt in db

    return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    esami = Esame.objects.all() # una select

    result = []
    for esame in esami:
        result.append (str(esame.data))
        
    return JsonResponse(result)

# Create your views here.
