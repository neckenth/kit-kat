import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Request

# Create your views here.
def index(request):
    my_requests = Request.objects.order_by('-start_date')[:10]
    print(my_requests)
    output = ', '.join([f"{(r.start_date).strftime('%b %d, %Y')}" for r in my_requests])
    return HttpResponse(output)


def detail(request, req_id):
    response = f"You're looking at request {req_id}"
    return HttpResponse(response)


def new(request):
    return HttpResponse("You're looking at the new request page")


