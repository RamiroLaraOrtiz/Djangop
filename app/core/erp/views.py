from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfirstview (request):
    data={
        'name': 'Ramiro'
    }
    return JsonResponse(data)
    #return HttpResponse('hola eta es mi priera url')