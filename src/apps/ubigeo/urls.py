from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ubigeo.views',
    url(r'^provincia/json/$', 'provincia', name='ubigeo-provincia-json'),
)
