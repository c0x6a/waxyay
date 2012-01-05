# -*- coding: utf-8 -*-
from django.shortcuts import render
from base.models import Base
from forms import BaseForm
from ciudadano.forms import CitizenForm

def registrar(request):
    baseform = BaseForm()
    if request.method == 'POST':
        baseform = BaseForm(request.POST)
        if baseform.is_valid():
            baseform.save()
            return redirect('/base/registrar/')
    #citizenform = CitizenForm()
    return render(request,
        'base/base.html',
        {'baseform' : baseform,})
