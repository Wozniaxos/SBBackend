from django.http import HttpResponse
import json

def index(request):
    return HttpResponse(json.loads('{"name": 2}'))
