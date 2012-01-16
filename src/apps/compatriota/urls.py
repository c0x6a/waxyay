from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('compatriota.views',
    url(r'^afiliar/$', 'afiliar', name='compatriota-afiliar'),
    url(r'^buscar/$', 'buscar', name='compatriota-buscar'),
)
