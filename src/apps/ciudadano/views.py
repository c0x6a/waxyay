# -*- coding: utf-8 -*-
from models import Citizen
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

@login_required(login_url='/profile/login/')
def dni_json(request, dni):
    ciudadano = Citizen.objects.get(number_document = dni)
    return HttpResponse(serializers.serialize('json',[ciudadano], ensure_ascii=False),mimetype='application/json')
