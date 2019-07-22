from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the kit kat index.")


def detail(request, req_id):
    response = f"You're looking at request {req_id}"
    return HttpResponse(response)


def new(request):
    return HttpResponse("You're looking at the new request page")


