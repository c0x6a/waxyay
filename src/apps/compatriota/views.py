# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from ciudadano.models import Citizen
from base.forms import BaseForm
from forms import AffiliateForm
from ciudadano.forms import CitizenForm

def afiliar(request):
    affiliateform = AffiliateForm()
    if request.method == 'POST':
        affiliateform = AffiliateForm(request.POST)
        if affiliateform.is_valid():
            affiliateform.save()
            return redirect("/compatriota/afiliar/")
    citizenform = CitizenForm()
    baseform = BaseForm()
    return render(request,
        'afiliado/afiliado.html',
        {'affiliateform' : affiliateform, 'citizenform' : citizenform, 'baseform' : baseform,})
