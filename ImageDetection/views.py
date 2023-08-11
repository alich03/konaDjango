

import requests
from django.http import HttpResponse

def home(request):
    return HttpResponse("this is ok. <h2>to apis </h2>")