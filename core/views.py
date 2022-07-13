import time

from django.shortcuts import render
from django.http import HttpResponse

from minicademic import settings

# Create your views here.

def home_view(request):
    return HttpResponse('Hello world! ' + str(time.process_time() - settings.start_time))
