# -*- encoding: utf-8 -*-
import urllib

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.template import Context, loader
from django.shortcuts import render
from django.core.context_processors import csrf

from google.appengine.api import users

from .models import UserDict

def top_page(request):
    html = "<html><body>It is now .</body></html>"
    return HttpResponse(html)

def nhk_program(request):
    pass
