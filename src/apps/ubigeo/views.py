# -*- coding: utf-8 -*-
from models import Ubigeo
from django.utils import simplejson
from django.core import serializers
from django.http import HttpResponse

json_serializer = serializers.get_serializer("json")()

def validate_ubigeo(value):
    print 'validando'
    print value
    obj, created = Ubigeo.objects.get_or_create(ubigeo = value)
    if created:
        raise ValidationError(u'%s no es valido' % value)

def provincia(request):
    provincias = Ubigeo.objects.filter(parent = Ubigeo.objects.get(ubigeo = request.GET['r'])).order_by('name')
    resultado = json_serializer.serialize(provincias, ensure_ascii=False)
    return HttpResponse(resultado,mimetype='application/json')

def distrito(request):
    distritos = Ubigeo.objects.filter(parent = Ubigeo.objects.get(ubigeo = request.GET['d'])).order_by('name')
    resultado = json_serializer.serialize(distritos, ensure_ascii=False)
    return HttpResponse(resultado,mimetype='application/json')
