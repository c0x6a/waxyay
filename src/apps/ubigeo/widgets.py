from django import forms
from django.forms.widgets import Select, MultiWidget
from models import Ubigeo

class UbigeoWidget(MultiWidget):
    
    def __init__(self, attrs=None):
        regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
        provincias = Ubigeo.objects.filter(parent=regiones[0]).order_by('name')
        distritos  = Ubigeo.objects.filter(parent=provincias[0]).order_by('name')
        widgets = (
            Select(
                choices = ((r.ubigeo, r.name) for r in regiones), attrs = {'onchange' : 'getProvincias(this.value);'}
            ),
            Select(
                choices = ((p.ubigeo, p.name) for p in provincias), attrs = {'onchange' : 'getDistritos(this.value);'}
            ),
            Select(
                choices = ((d.ubigeo, d.name) for d in distritos)
            )
        )
        super(UbigeoWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        print 'entro!!!!!!!!!!!!'
        print value
        if value:
            regiones   = Ubigeo.objects.filter(parent__isnull=True)
            provincias = Ubigeo.objects.filter(parent=regiones[0])
            distritos  = Ubigeo.objects.filter(parent=provincias[0])
            return (regiones.ubigeo, provincias.ubigeo, distritos.ubigeo)
        else:
            return (None, None, None)
