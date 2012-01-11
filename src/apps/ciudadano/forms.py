from django import forms
from django.forms.widgets import RadioSelect, TextInput
from django.utils.safestring import mark_safe
from django.forms.extras.widgets import SelectDateWidget
from models import Citizen
import datetime

GENDER_CHOICES = (
    (u'M', u'Masculino'),
    (u'F', u'Femenino'),
)

class HorizRadioRenderer(forms.RadioSelect.renderer):

    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class CitizenForm(forms.ModelForm):

    class Meta:
        model = Citizen
        widgets = {
            'birth_date' : SelectDateWidget(years = [(year) for year in range(1935, datetime.date.today().year)]),
            'sex' : RadioSelect(choices = GENDER_CHOICES, renderer=HorizRadioRenderer),
            'number_document' : TextInput(attrs = {'onKeyPress':'if(event.keyCode==13) {getCiudadano(this.value);}return false;'}),
        }

    class Media:
        js = (
            "js/ciudadano.js",
            )
