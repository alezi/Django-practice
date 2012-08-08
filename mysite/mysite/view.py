from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hellow world!")
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours = offset)
    assert False
    html = "<html><body><h1>In %s hours ,It will be %s</h1></body></html"% (offset,dt)
    return HttpResponse(html)
