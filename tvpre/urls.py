from django.conf.urls import patterns, include, url
from tvpre.views import top_page, nhk_program

urlpatterns = patterns('',
    (r'^programs/$', nhk_program),
    (r'^$', top_page),
)
