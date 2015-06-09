from django.conf.urls import patterns, url

from fm import views
urlpatterns = patterns('',
                       #url(r'^$', views.profile, name='profile'),
                       url(r'^$', views.login_user),
                       url(r'^save/', views.save),
                       url(r'^logout/', views.logout_view),
                       url(r'^profile/', views.profile),
                       url(r'^profileedit/', views.profile_edit),
                       url(r'^saveprofile/', views.saveprofile),
                       url(r'^changepassword/', views.changepassword),
                       url(r'^passwordchanged/', views.passwordchanged),
                       )
