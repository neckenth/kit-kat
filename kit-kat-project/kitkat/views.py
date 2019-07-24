# import datetime as dt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Request


# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    #todo: add more fields to form for team and employee type
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {
        "form": form
    })


# def index(request):
#     my_requests = Request.objects.order_by('-start_date')[:10]
#     output = ', '.join(
#         [f"{(r.start_date).strftime('%b %d, %Y')}" for r in my_requests])
#     return HttpResponse(output)


# def detail(request, req_id):
#     response = f"You're looking at request {req_id}"
#     return HttpResponse(response)


# def new(request):
#     return HttpResponse("You're looking at the new request page")
