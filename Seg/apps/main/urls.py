__author__ = 'asilvio'
from django.conf.urls import patterns, url

urlpatterns = patterns('Seg.apps.main.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^contact/$', 'contact_view', name='contact'),
    url(r'^mattress/$', 'mattress_view', name='mattress'),
    url(r'^mattress/(?P<num>[0-9]+)$', 'mattress2_view', name='mattress2'),
    url(r'^youth/(?P<num>[0-9]+)$', 'youthc_view', name='youthc'),
    url(r'^youth/2/(?P<num>[0-9]+)$', 'youth_art_view', name='youth_art'),
    url(r'^youth/$', 'youth_view', name='youth'),
    url(r'^bedroom/$', 'bedroom_view', name='bedroom'),
    url(r'^bedroom/(?P<num>[0-9]+)$', 'bedroom2_view', name='bedroom2'),
    url(r'^diningroom/$', 'diningroom_view', name='diningroom'),
    url(r'^diningroom/(?P<num>[0-9]+)$', 'diningroom2_view', name='diningroom2'),
    url(r'^livingroom/$', 'livingroom_view', name='livingroom'),
    url(r'^livingroom/(?P<num>[0-9]+)$', 'livingroom2_view', name='livingroom2'),
)
