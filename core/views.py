from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    
    return HttpResponse("Welcome to Nexus")


def health_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})
