# -*- coding: utf-8 -*-
from models import Citizen
from django.utils import simplejson
from django.core import serializers
from django.http import HttpResponse

json_serializer = serializers.get_serializer("json")()

def dni_json(request, dni):
    provincias = Citizen.objects.get(number_document = dni)
    resultado = json_serializer.serialize(provincias, ensure_ascii=False)
    return HttpResponse(resultado,mimetype='application/json')
