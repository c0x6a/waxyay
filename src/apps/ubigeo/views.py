# -*- coding: utf-8 -*-
from models import Ubigeo
from django.core import serializers
from django.http import HttpResponse

def provincia(request):
    provincias = Ubigeo.objects.filter(parent = Ubigeo.objects.get(ubigeo = request.GET['r'])).order_by('name')
    return HttpResponse(serializers.serialize("json", provincias, ensure_ascii=False),mimetype='application/json')

def distrito(request):
    distritos = Ubigeo.objects.filter(parent = Ubigeo.objects.get(ubigeo = request.GET['d'])).order_by('name')
    return HttpResponse(serializers.serialize("json", distritos, ensure_ascii=False),mimetype='application/json')
