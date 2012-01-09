from django.contrib import admin
from models import Citizen

class CitizenAdmin(admin.ModelAdmin):
    #list_display   = ('profile','title','date_posted','only_users')
    #list_filter    = ['profile','date_posted','only_users','authorize']
    #search_fields  = ['title','content']
    list_per_page = 25
    list_max_show_all = 30
    #date_hierarchy = 'date_posted'

admin.site.register(Citizen, CitizenAdmin)
