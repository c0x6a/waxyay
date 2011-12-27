from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('afiliado.views',
    url(r'^afiliar/$', 'afiliar', name='afiliado-afiliar'),
)
