# -*- coding: utf-8 -*-
from django.shortcuts import render
from ciudadano.models import Citizen
from base.forms import BaseForm
from forms import AffiliateForm
from ciudadano.forms import CitizenForm

def afiliar(request):
    affiliateform = AffiliateForm()
    citizenform = CitizenForm()
    baseform = BaseForm()
    return render(request,
        'afiliado/afiliado.html',
        {'affiliateform' : affiliateform, 'citizenform' : citizenform, 'baseform' : baseform,})
