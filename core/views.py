from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Game

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    
    return HttpResponse("Welcome to Nexus")


def health_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})

def game_list(request: HttpRequest) -> HttpResponse:
    games = Game.objects.all()
    
    return render(request, "core/game_list.html", {"games": games})