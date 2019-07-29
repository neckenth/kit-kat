# import datetime as dt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, TimeOffRequestForm
from .models import Request, Profile


# Create your views here.

@login_required
def home(request):
    # todo - next piece is to add a button in home
    # this button should open a page with a form for a new time-off request and set up the PDF and smtp
    # then the calendar view w/ clickable elements
    return render(request, 'home.html')


def signup(request):
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
    return render(request, 'registration/signup.html', {
        "form": form
    })


@login_required
def new_request(request):
    if request.method == "POST":
        form = TimeOffRequestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = Profile.objects.get(user=request.user)
            instance.save()
            return HttpResponseRedirect('/kitkat/')
    else:
        form = TimeOffRequestForm()
    return render(request, 'request_form.html', {'form': form})


# def view_requests(request):
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
