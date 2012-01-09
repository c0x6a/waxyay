from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('base.views',
    url(r'^registrar/$', 'registrar', name='base-registrar'),
    url(r'^compatriota/$', 'base_compatriota', name='base-compatriota'),
    url(r'^search/$', 'search', name='base-search'),
    url(r'^add/$', 'registrar_add', name='base-add'),
)
