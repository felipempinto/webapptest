from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def homepage(request):
    hour = datetime.now().strftime(format='%d/%m/%Y %H:%M:%S')
    s = f"Hey JOVAAAAAAAAAAAAAAANIA, this is a <b>test</b> web page, the last refresh was made at <b>{hour}</b>"
    return HttpResponse(s)