from django import forms
from models import Affiliate
from django.forms.widgets import RadioSelect, HiddenInput
from django.forms.extras.widgets import SelectDateWidget
from ubigeo.fields import UbigeoField
from ubigeo.models import Ubigeo

class AffiliateForm(forms.ModelForm):

    ubigeo = UbigeoField()

    def __init__(self, *args, **kwargs):
        super(AffiliateForm, self).__init__(*args, **kwargs)
        if self.data:
            regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
            provincias = Ubigeo.objects.filter(parent=self.data['ubigeo_0']).order_by('name')
            distritos  = Ubigeo.objects.filter(parent=self.data['ubigeo_1']).order_by('name')
            self.fields['ubigeo'].fields[0].queryset = regiones
            self.fields['ubigeo'].fields[1].queryset = provincias
            self.fields['ubigeo'].fields[2].queryset = distritos

    class Meta:
        model = Affiliate
        widgets = {
            'date_enrollment' : SelectDateWidget(),
            'base' : HiddenInput(),
        }

    class Media:
        js = (
            "js/ubigeo.js",
            "js/compatriota.js",
            )
