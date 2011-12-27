from django import forms
from django.forms.widgets import Select, MultiWidget
from models import Ubigeo

class UbigeoWidget(MultiWidget):
    
    def __init__(self, attrs=None):
        widgets = (
            Select(),Select(),Select()
        )
        super(UbigeoWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            d = strftime("%Y-%m-%d", value.timetuple())
            hour = strftime("%I", value.timetuple())
            minute = strftime("%M", value.timetuple())
            return (d, hour, minute, meridian)
        else:
            return (None, None, None)
