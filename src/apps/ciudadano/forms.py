from django import forms
from models import Citizen

class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
