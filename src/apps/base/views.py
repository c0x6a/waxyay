# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from base.models import Base
from ubigeo.models import Ubigeo
from forms import BaseForm
from ciudadano.forms import CitizenForm

@login_required(login_url='/profile/login/')
def search_base(request):
    if 'ubigeo_2' in request.POST:
        ubigeo = Ubigeo.objects.get(ubigeo = request.POST['ubigeo_2'])
        return Base.objects.filter(Q(active = True),Q(name__icontains = request.POST['base_name']),Q(ubigeo = ubigeo))
    elif 'ubigeo_1' in request.POST:
        ubigeos = Ubigeo.objects.get(parent = Ubigeo.objects.get(request.POST['ubigeo_1']))
        return Base.objects.filter(Q(active = True),Q(name__icontains = request.POST['base_name']),Q(ubigeo__in = ubigeos))
    elif 'ubigeo_0' in request.POST:
        ubigeos = Ubigeo.objects.get(parent__in = Ubigeo.objects.filter(parent = Ubigeo.objects.get(request.POST['ubigeo_0'])))
        return Base.objects.filter(Q(active = True),Q(name__icontains = request.POST['base_name']),Q(parent__in = ubigeos))

@login_required(login_url='/profile/login/')
def registrar(request):
    baseform = BaseForm()
    if request.method == 'POST':
        baseform = BaseForm(request.POST)
        if baseform.is_valid():
            baseform.save()
            return redirect('/base/registrar/')
    return render(request,
        'base/base.html',
        {'baseform' : baseform,'auth':request.user,})

@login_required(login_url='/profile/login/')
def base_compatriota(request):
    baseform = BaseForm()
    if request.method == 'POST':
        bases = search_base(request)
        return render(request,
            'base/base-compatriota.html',
            {'baseform' : baseform,'bases' : bases})
    return render(request,
        'base/base-compatriota.html',
        {'baseform' : baseform,})

@login_required(login_url='/profile/login/')
def registrar_add(request):
    baseform = BaseForm(request.POST)
    if baseform.is_valid():
        baseform.save()
    return render(request,
        'base/base-to-compatriota.html',
        {'base' : baseform.instance,})

@login_required(login_url='/profile/login/')
def search(request):
    return None
