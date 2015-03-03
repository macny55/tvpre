from django.conf.urls import patterns, include, url
from tvpre.views import top_page

urlpatterns = patterns('',
    (r'^$', top_page),
)
