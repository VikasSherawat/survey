from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<q_num>[0-9A-Za-z]+)/$', views.detail, name='detail'),
    url(r'^(?P<q_num>[0-9A-Za-z]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<q_num>[0-9A-Za-z]+)/result/$', views.result, name='result'),
]