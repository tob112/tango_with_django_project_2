from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^/about$', about, name='page'),
                       url(r'category/(?P<category_name_url>\w+)/$', category, name='category'),
                       )
