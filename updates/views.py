import json
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
from django.views.generic import View

from .mixins import JsonResponseMixin

def json_example_view(request):
    '''
    URI -- for REST
    GET request
    '''
    data = {
        "count": 1000,
        "content": "sudo"
    }
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(data)

class SerializeDetailView(View):
    '''its a class Base View'''
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id =1)
        json_data = obj.serialize()
        return JsonResponse(data)



class SerializeListView(View):
        def get(self, request, *args, **kwargs):
            qs = Update.objects.all()
            return HttpResponse(json_data, content_type = 'application/json')
            
