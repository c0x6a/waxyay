from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ciudadano.views',
    url(r'^(?P<dni>\d+)/json/$', 'dni_json', name='ciudadano-dni-json'),
)
