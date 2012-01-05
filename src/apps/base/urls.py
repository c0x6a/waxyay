from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('base.views',
    url(r'^registrar/$', 'registrar', name='base-registrar'),
)
