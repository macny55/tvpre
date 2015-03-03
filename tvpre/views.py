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
from .utils  import ProgramList

def top_page(request):
    html = "<html><body>It is now .</body></html>"
    return HttpResponse(html)

def nhk_program(request):
    service = ['g1']
    client = ProgramList(user_id = 'macny55')
    content = Context({'pg_list' : client.recommend_pg_list('130',service)})
    return HttpResponse(loader.get_template('program.html').render(content))

