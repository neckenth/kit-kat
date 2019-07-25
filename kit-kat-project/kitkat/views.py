# import datetime as dt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from .models import Request


# Create your views here.

def home(request):
    # todo - next piece is to add a button in home
    # this button should open a page with a form for a new time-off request and set up the PDF and smtp
    # then the calendar view w/ clickable elements
    return render(request, 'home.html')


def signup(request):
    # todo - login endpoint
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
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
