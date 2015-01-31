from django.conf.urls import patterns, url

from web.extractor.views import home


urlpatterns = patterns('',
                       url(r'/?$', home.home_view, name='home_page'),
)