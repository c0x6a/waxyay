from django import forms
from django.forms.widgets import Select, MultiWidget
from models import Ubigeo

class UbigeoWidget(MultiWidget):
    
    def __init__(self, regiones, provincias, distritos):
        #print dir(self)
        #if ubigeo is None:
        #    regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
        #    provincias = Ubigeo.objects.filter(parent=regiones[0]).order_by('name')
        #    distritos  = Ubigeo.objects.filter(parent=provincias[0]).order_by('name')
        #else:
        #    distrito   = Ubigeo.objects.get(ubigeo = ubigeo)
        #    regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
        #    provincias = Ubigeo.objects.filter(parent=distrito.parent.parent).order_by('name')
        #    distritos  = Ubigeo.objects.filter(parent=distrito.parent).order_by('name')
        widgets = (
            Select(
                choices = regiones, attrs = {'onchange' : 'getProvincias(this.value);'}
            ),
            Select(
                choices = provincias, attrs = {'onchange' : 'getDistritos(this.value);'}
            ),
            Select(
                choices = distritos
            )
        )
        super(UbigeoWidget, self).__init__(widgets)

    def decompress(self, value):
        print 'entro!!!!!!!!!!!!'
        print value
        #if value:
            #regiones   = Ubigeo.objects.filter(parent__isnull=True)
            #provincias = Ubigeo.objects.filter(parent=regiones[0])
            #distritos  = Ubigeo.objects.filter(parent=provincias[0])
        #    return (None, None, None)
        #else:
        return value, value, value
