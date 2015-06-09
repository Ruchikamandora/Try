from django.conf.urls import patterns, url
from ds import views
urlpatterns = patterns('',
                       #url(r'^$', views.profile, name='profile'),
                       url(r'^$', views.search),
                       url(r'^bsearch/', views.bsearch),
                       url(r'^(?P<num1>\d{2})/(?P<num2>\d{2})/(?P<num3>\d{2})/(?P<num4>\d{2})/(?P<num5>\d{2})/(?P<num6>\d{2})/(?P<nums>\d{2})/', views.bsearch2),
                       )
