from django import forms
from models import Ubigeo

class UbigeoForm(forms.ModelForm):
    class Meta:
        model = Ubigeo
