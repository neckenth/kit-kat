from typing import Tuple
import datetime as dt
import pytest
from django.contrib.auth import get_user_model
from .models import Profile, Request


User = get_user_model()


def add_user() -> Tuple[User, Profile]:
    """
    Since Users and Profiles are created in tandem and are related to other 
    models as ForeignKeys, return a Tuple of both instances
    """
    user = User.objects.create(
        first_name="tester", last_name="mctestface", username="test@test.com")
    return (
        user,
        Profile.objects.get(
            first_name=user.first_name, last_name=user.last_name
        )
    )


@pytest.fixture
def request_obj_1(add_user):
    return Request.objects.create(user=add_user[1], start_date=dt.datetime(2019, 12, 23, 12), end_date=dt.datetime(2019, 12, 26, 5))
