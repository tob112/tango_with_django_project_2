from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
                       url(r'^/$', index, name='index'),
                       url(r'^/about/$', about, name='page'),
                       url(r'^/add_category/$', add_category, name='add_category'),
                       url(r'category/(?P<category_name_url>\w+)/$', category, name='category'),
                       url(r'category/(?P<category_name_url>\w+)/add_page/$', add_page, name='add_page'),
                       url(r'^/register/$', register, name='register'),
                       url(r'^/login/$', user_Login, name='login'),
                       url(r'^/restricted/$', restricted, name='restricted'),
                       url(r'^/logout/$', user_logout, name='logout')
                       )
