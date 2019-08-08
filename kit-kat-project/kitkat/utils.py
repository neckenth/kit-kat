from .models import Request, Profile
from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()


def is_manager(user):
    return Profile.objects.get(user=user).user_type == "MAN"


def filter_requests(user):
    if not is_manager(user):
        return Request.objects.filter(user=Profile.objects.get(user=user)).order_by('-start_date')
    else:
        team = Profile.objects.get(user=user).team
        # print(team)
        print(Profile.objects.filter(team=team))
        print(Request.objects.filter(user__in=Profile.objects.filter(team=team)))
        return Request.objects.filter(user__in=Profile.objects.filter(team=team)).order_by('-start_date')
