from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignUpForm, TimeOffRequestForm
from .models import Profile, Request


@login_required
def home(request):
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


@login_required
def index(request):
    my_requests = Request.objects.filter(
        user=Profile.objects.get(user=request.user)).order_by('-start_date')
    # output = ', '.join(
        # [f"{(r.start_date).strftime('%b %d, %Y')}" for r in my_requests])
    return render(request, 'requests.html', {"my_requests_list": my_requests})


@login_required
def detail(request, req_id):
    output = get_object_or_404(Request, pk=req_id)
    return HttpResponse(output)
