# -*- coding: utf-8 -*-
from models import Citizen
from django.core import serializers
from django.http import HttpResponse

def dni_json(request, dni):
    ciudadano = Citizen.objects.get(number_document = dni)
    return HttpResponse(serializers.serialize('json',[ciudadano], ensure_ascii=False),mimetype='application/json')
