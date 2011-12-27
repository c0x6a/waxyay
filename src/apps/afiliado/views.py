# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import AffiliateForm

def afiliar(request):
    affiliateform = AffiliateForm()
    return render(request,
        'afiliado/afiliado.html',
        {'form' : affiliateform})
