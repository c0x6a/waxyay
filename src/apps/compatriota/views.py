# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ciudadano.models import Citizen
from base.forms import BaseForm
from base.models import Base
from forms import AffiliateForm
from models import Affiliate
from ubigeo.forms import UbigeoSelect
from ciudadano.forms import CitizenForm
from ciudadano.models import Citizen
from historial.models import Record
import datetime

@login_required(login_url='/profile/login/')
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
        {'affiliateform' : affiliateform, 'citizenform' : citizenform, 'baseform' : baseform,'auth':request.user,})

@login_required(login_url='/profile/login/')
def buscar(request):
    ubigeo = UbigeoSelect()
    if request.method == 'POST':
        if 'dni' in request.POST:
            affiliate = Affiliate.objects.get(citizen = Citizen.objects.get( pk = request.POST['dni']))
        elif 'nombre' in request.POST or 'apellido' in request.POST:
            nombre = request.POST['nombre'] if 'nombre' in requNoneest.POST else ''
            apellido = request.POST['apellido'] if 'apellido' in request.POST else ''
            affiliate = Affiliate.objects.filter(citizen__in = Citizen.objects.filter((Q(paternal_surname__icontains = request.POST['apellido']) | Q(mother_surname__icontains = request.POST['apellido'])) | Q(name__icontains = request.POST['nombre'])))
        elif 'base' in request.POST or 'id_base' in request.POST:
            if 'base' in request.POST:
                affiliate = Affiliate.objects.filter(base = Base.objects.get(pk = request.POST['id_base']))
            elif 'id_base' in request.POST:
                affiliate = Affiliate.objects.filter(base__in = Base.objects.filter(name__icontains = request.POST['base']))
        else:
            affiliate = None
            ubigeos = None
            if 'ubigeo_2' in request.POST or 'ubigeo_1' in request.POST or 'ubigeo_0' in request.POST:
                if 'ubigeo_2' in request.POST:
                    ubigeos = Ubigeo.objects.get(ubigeo = request.POST['ubigeo_2'])
                elif 'ubigeo_1' in request.POST:
                    ubigeos = Ubigeo.objects.get(parent = Ubigeo.objects.get(request.POST['ubigeo_1']))
                elif 'ubigeo_0' in request.POST:
                    ubigeos = Ubigeo.objects.get(parent__in = Ubigeo.objects.filter(parent = Ubigeo.objects.get(request.POST['ubigeo_0'])))
                affiliate =  Affiliate.objects.filter(ubigeo__in = ubigeos) if affiliate is None else affiliate.filter(ubigeo__in = ubigeos)
            if 'inicio' in request.POST or 'fin' in request.POST:
                if 'inicio' in request.POST and 'fin' in request.POST:
					affiliate =  Affiliate.objects.filter(citizen = Citizen.objects.filter(birth_date__year__range = ((datetime.datetime.today().year - request.POST['fin']), (datetime.datetime.today().year - request.POST['inicio'])))) if affiliate is None else affiliate.filter(citizen = Citizen.objects.filter(birth_date__year__range = ((datetime.datetime.today().year - request.POST['fin']), (datetime.datetime.today().year - request.POST['inicio']))))
                if 'inicio' in request.POST:
                    affiliate =  Affiliate.objects.filter(citizen__in = Citizen.objects.filter(birth_date__year = (datetime.datetime.today().year - request.POST['inicio']))) if affiliate is None else affiliate.filter(citizen__in = Citizen.objects.filter(birth_date__year = (datetime.datetime.today().year - request.POST['inicio'])))
                if 'fin' in request.POST:
                    affiliate =  Affiliate.objects.filter(citizen__in = Citizen.objects.filter(birth_date__year = (datetime.datetime.today().year - request.POST['fin']))) if affiliate is None else affiliate.filter(citizen__in = Citizen.objects.filter(birth_date__year = (datetime.datetime.today().year - request.POST['fin'])))
            if 'profesion' in request.POST:
                affiliate =  Affiliate.objects.filter(pk__in = Record.objects.values('affiliate').filter((Q(category = 4)|Q(category = 5)),Q(description__icontains = request.POST['profesion']))) if affiliate is None else affiliate.filter(pk__in = Record.objects.values('affiliate').filter((Q(category = 4)|Q(category = 5)),Q(description__icontains = request.POST['profesion'])))
            if 'tipo' in request.POST:
                affiliate =  Affiliate.objects.filter(kind = request.POST['tipo']) if affiliate is None else affiliate.filter(kind = request.POST['tipo'])
            if 'estado' in request.POST:
                affiliate =  Affiliate.objects.filter(state = request.POST['estado']) if affiliate is None else affiliate.filter(state = request.POST['estado'])
        return render(request,
        'afiliado/buscar.html',
        {'ubigeo' : ubigeo, 'affiliate':affiliate,'auth':request.user,})
    return render(request,
        'afiliado/buscar.html',
        {'ubigeo' : ubigeo,'auth':request.user,})
