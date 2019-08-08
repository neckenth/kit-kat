from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime as dt, date, timedelta
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import SignUpForm, TimeOffRequestForm
from .models import Profile, Request
from .calendar import Calendar
from .utils import filter_requests
import calendar


def get_date(day):
    if day:
        year, month = (int(x) for x in day.split('-'))
        return date(year=year, month=month, day=1)
    return dt.today()


def prev_month(date):
    first_day_curr_month = date.replace(day=1)
    last_day_prev_month = first_day_curr_month - timedelta(days=1)
    return f"month={last_day_prev_month.year}-{last_day_prev_month.month}"


def next_month(date):
    total_days_curr_month = calendar.monthrange(date.year, date.month)[1]
    first_day_curr_month = date.replace(day=1)
    first_day_next_month = first_day_curr_month + \
        timedelta(days=total_days_curr_month)
    return f"month={first_day_next_month.year}-{first_day_next_month.month}"


class CalendarView(generic.ListView):
    model = Request
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))

        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        cal = Calendar(d.year, d.month)
        cal.setfirstweekday(6)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


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
    my_requests = filter_requests(request.user)
    return render(request, 'requests.html', {"my_requests_list": my_requests})


@login_required
def detail(request, req_id):
    req = get_object_or_404(Request, pk=req_id)
    return render(request, 'one_request.html', {"this_request": req})
