from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'facultyM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^faculty/', include('fm.urls')),
    url(r'^login/', include('fm.urls')),
    url(r'^pfaculty/', include('pconspectus.urls')),
    url(r'^tlogin/', include('pconspectus.urls')),
    url(r'^plogin/', include('pconspectus.urls')),
    url(r'^search/', include('ds.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
