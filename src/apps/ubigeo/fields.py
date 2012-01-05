from django import forms
from django.forms import ModelChoiceField
from django.core.exceptions import ValidationError
from widgets import UbigeoWidget
from models import Ubigeo
from ubigeo.views import validate_ubigeo

class UbigeoField(forms.MultiValueField):
    
    def __init__(self, required=True, *args, **kwargs):
        regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
        provincias = Ubigeo.objects.filter(parent=regiones[0]).order_by('name')
        distritos  = Ubigeo.objects.filter(parent=provincias[0]).order_by('name')
        fields = (
            ModelChoiceField(queryset=regiones),
            ModelChoiceField(queryset=provincias),
            ModelChoiceField(queryset=distritos)
        )
        widget = UbigeoWidget(regiones = fields[0]._get_choices(), provincias = fields[1]._get_choices(), distritos = fields[2]._get_choices())
        #self._was_required = kwargs.pop('required', True)
        super(UbigeoField, self).__init__(fields, required, widget, *args, **kwargs)

    #def clean(self, *args, **kwargs):
    #    lista = super(UbigeoField, self).clean(*args, **kwargs)
    #    return lista

    #def to_python(self, value):
    #    print 'dataaaaaaa'
    #    print value
        # Return an empty list if no input was given.
    #    if not value:
    #        return []
    #    return value

    #def validate(self, value):
        # Use the parent's handling of required fields, etc.
        #super(UbigeoField, self).validate(value)
    #    print value

    def compress(self, data_list):
        if data_list:
            return data_list[2]
        return None
