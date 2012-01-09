# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Base
from forms import BaseForm

class BaseAdmin(admin.ModelAdmin):
    list_display   = ('name','foundation','ubigeo','active')
    #list_filter    = ['profile','date_posted','only_users','authorize']
    #search_fields  = ['title','content']
    list_per_page = 25
    list_max_show_all = 30
    #date_hierarchy = 'date_posted'
    form = BaseForm
    
admin.site.register(Base, BaseAdmin)
