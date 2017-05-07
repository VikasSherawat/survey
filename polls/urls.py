from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^survey/', include('survey.urls')),
    url(r'^polls/', include('createpolls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^googlelogin/', views.googlelogin, name = 'googlelogin'),
]
