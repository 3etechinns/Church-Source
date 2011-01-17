import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    ('^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '%sfavicon.ico' % settings.MEDIA_URL}),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += patterns('churchsource.people.views',
  url(r'^jpegcam/$', 'jpegcam_admin', name='cs_jpegcam'),
)

if settings.DEBUG:
  urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': os.path.join(settings.SPATH, 'static'), 'show_indexes': True}),
  )
  
if settings.THUMBNAIL_DUMMY:
  urlpatterns += patterns('',
    (r'^', include('sorl.thumbnail.urls')),
  )
  