# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Affiliate

class PostAdmin(admin.ModelAdmin):
    list_display   = ('profile','title','date_posted','only_users')
    list_filter    = ['profile','date_posted','only_users','authorize']
    search_fields  = ['title','content']
    list_per_page = 25
    list_max_show_all = 30
    date_hierarchy = 'date_posted'

    class Media:
        js = ('tiny_mce/tiny_mce.js',
                'js/textarea.js',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.profile = Profile.objects.get(user = request.user)
        obj.save()

    def queryset(self, request):
        qs = super(PostAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(profile=Profile.objects.get(user = request.user))

    def add_view(self, request, form_url='', extra_context=None):
        self.fields = ('title','content','only_users','authorize') if request.user.is_superuser else ('title','content','only_users')
        return super(PostAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, extra_context=None):
        self.fields = ('title','content','only_users','authorize') if request.user.is_superuser else ('title','content','only_users')
        return super(PostAdmin, self).change_view(request, object_id, extra_context=None)

admin.site.register(Affiliate)
