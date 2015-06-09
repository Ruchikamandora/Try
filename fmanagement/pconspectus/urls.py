from django.conf.urls import patterns, url
from pconspectus import views
urlpatterns = patterns('',
                       #url(r'^$', views.profile, name='profile'),
                       url(r'^$', views.login_user),
                       url(r'^save/', views.save),
                       url(r'^profile/', views.profile),
                       url(r'^logout/', views.logout_view),
                       url(r'^changepassword/', views.changepassword),
                       url(r'^passwordchanged/', views.passwordchanged),
                       url(r'^pedit', views.pedit),
                       url(r'^userlogin', views.userlogin),
                       url(r'^adminlogin', views.adminlogin),
                       url(r'^developer', views.developer),
                       url(r'^createprofile/', views.createprofile),
                       url(r'^deleteform/', views.deleteform),
                       url(r'^rpaper/', views.rpaper),
                       url(r'^book/', views.book),
                       url(r'^bookchapter/', views.bookchapter),
                       url(r'^cpaper/', views.cpaper),
                       url(r'^booksave/', views.booksave),
                       url(r'^bookchaptersave/', views.bookchaptersave),
                       url(r'^rpapersave/', views.rpapersave),
                       url(r'^cpapersave/', views.cpapersave),
                       url(r'^myuploads/', views.myuploads),
                       url(r'^Myalluploads/', views.Myalluploads),
                       url(r'^search/', views.search),
                       url(r'^advancedsearch/', views.advancedsearch),
                       url(r'^advanceysearch/', views.advanceysearch),
                       url(r'^advanceasearch/', views.advanceasearch),
                       url(r'^name/(?P<name>[^/]+)/$', views.name),
                       url(r'^(?P<title>.+)/$', views.title),
                       )