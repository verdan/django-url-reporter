from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import web.extractor.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'report.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(web.extractor.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
