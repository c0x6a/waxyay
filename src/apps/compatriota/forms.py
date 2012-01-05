from django import forms
from models import Affiliate
from django.forms.extras.widgets import SelectDateWidget
from ubigeo.widgets import UbigeoWidget
import datetime

class AffiliateForm(forms.ModelForm):
    class Meta:
        model = Affiliate
        widgets = {
            'date_birth' : SelectDateWidget(years = [(year) for year in range(1965, datetime.date.today().year)]),
            #'ubigeo_now' : UbigeoWidget(),
            'date_enrollment' : SelectDateWidget(),
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
