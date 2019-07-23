import datetime as dt
from typing import Tuple
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Profile, Request

User = get_user_model()
# Create your tests here.

def add_user() -> Tuple[User, Profile]:
    user = User.objects.create(first_name="tester", last_name="mctestface", username="test@test.com")
    return (user, Profile.objects.get(first_name=user.first_name, last_name=user.last_name))

class UserModelTests(TestCase):
    def test_profile_created_with_user(self):
        """
        When a User object is created, a Profile object should be created in tandem with same data
        """
        profile = add_user()[1]
        # profile = Profile.objects.get(first_name="tester", last_name="mctestface")
        assert profile is not None

class RequestModelTests(TestCase):
    def test_get_hours(self):
        """
        The number of hours between a start and end date
        """
        profile = add_user()[1]
        request_1 = Request.objects.create(user=profile, end_date = dt.datetime(2013, 12, 26, 5), start_date = dt.datetime(2013, 12, 23, 12))

