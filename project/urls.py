
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # grapelli admin urls
    (r'^grappelli/', include('grappelli.urls')),
    (r'^compatriota/', include('compatriota.urls')),
    (r'^ubigeo/', include('ubigeo.urls')),
    #(r'^$', include('home.urls')),
    (r'^$', 'home.views.index'),
)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$',
            serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^favicon\.ico$', 
            'django.views.generic.simple.redirect_to', 
            {'url': '/static/images/favicon.ico'}),
    )
