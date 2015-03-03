from django.conf.urls import patterns, include, url
from tvpre.views import main_page

urlpatterns = patterns('',
    (r'^$', main_page),
)
