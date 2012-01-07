from django import forms
from django.forms.extras.widgets import SelectDateWidget
from ubigeo.models import Ubigeo
from ubigeo.widgets import UbigeoWidget
from ubigeo.fields import UbigeoField
from ubigeo.views import validate_ubigeo
from models import Base
import datetime

class BaseForm(forms.ModelForm):
    
    ubigeo = UbigeoField()
    
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        if len(self.data) > 0:
            regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
            provincias = Ubigeo.objects.filter(parent=self.data['ubigeo_0']).order_by('name')
            distritos  = Ubigeo.objects.filter(parent=self.data['ubigeo_1']).order_by('name')
            self.fields['ubigeo'].fields[0].queryset = regiones
            self.fields['ubigeo'].fields[1].queryset = provincias
            self.fields['ubigeo'].fields[2].queryset = distritos

    class Meta:
        model = Base
        widgets = {
            'foundation' : SelectDateWidget(years = [(year) for year in range(2005, datetime.date.today().year + 1 )]),
        }
    
    class Media:
        css = {
            'screen' : ('css/jquery-ui.css',),
            }
        js = (
            "js/jquery.js",
            "js/jquery-ui.js",
            "js/ubigeo.js",
            )
