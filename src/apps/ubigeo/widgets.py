from django import forms
from django.forms.widgets import Select, MultiWidget
from models import Ubigeo

class UbigeoWidget(MultiWidget):

    def __init__(self, regiones, provincias, distritos):
        widgets = (
            Select(
                choices = regiones, attrs = {'onchange' : 'getProvincias(this.value, null, null);'}
            ),
            Select(
                choices = provincias, attrs = {'onchange' : 'getDistritos(this.value, null);'}
            ),
            Select(
                choices = distritos
            )
        )
        super(UbigeoWidget, self).__init__(widgets)

    def decompress(self, value):
        if value:
            ubigeo = Ubigeo.objects.get(ubigeo = value)
            self.widgets[1] = Select(choices = ((u.ubigeo, u.name) for u in Ubigeo.objects.filter(parent = ubigeo.parent.parent)), attrs = {'onchange' : 'getDistritos(this.value);'})
            self.widgets[2] = Select(choices = ((u.ubigeo, u.name) for u in Ubigeo.objects.filter(parent = ubigeo.parent)))
            return (ubigeo.parent.parent.ubigeo, ubigeo.parent.ubigeo, ubigeo.ubigeo)
        return (None, None, None)
