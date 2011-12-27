# -*- coding: utf-8 -*-
from models import Ubigeo
from django.utils import simplejson
from django.http import HttpResponse

def provincia(request):
    provincias = Ubigeo.objects.filter(parent = request.GET['r'])
    return HttpResponse(simplejson.dumps(provincias),mimetype='application/json')
