import datetime as dt
import pytest
from typing import Tuple
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Profile, Request

User = get_user_model()
# Create your tests here.


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
        The number of hours between a start and end date should be correctly...
        ...calculated per MA holidays and AdmitHub business hours
        This data should be properly saved to Request document upon save
        """
        profile = add_user()[1]
        request_1 = Request.objects.create(
            user=profile,
            start_date=dt.datetime(2019, 12, 23, 12),
            end_date=dt.datetime(2019, 12, 26, 5)
        )
        # accounting for starting mid-day, national holiday, and ending prior to day start
        assert request_1.hours == 13

    def test_is_in_future(self):
        """
        `is_in_future()` should correctly return True if start_date of request is in the future

        """
        profile = add_user()[1]
        request_1 = Request.objects.create(
            user=profile,
            start_date=dt.datetime(2019, 12, 23, 12),
            end_date=dt.datetime(2019, 12, 26, 5)
        )
        assert request_1.is_in_future()
        request_2 = Request.objects.create(
            user=profile,
            start_date=dt.datetime(2019, 1, 23, 12),
            end_date=dt.datetime(2019, 1, 26, 5)
        )
        assert not request_2.is_in_future()

    def test_invalid_request(self):
        """
        If a user enter's a start date that is later then the end date,
        a ValidationError will be raised
        """
        profile = add_user()[1]
        with pytest.raises(ValidationError):
            Request.objects.create(
                user=profile,
                start_date=dt.datetime(2020, 3, 23, 12),
                end_date=dt.datetime(2020, 1, 26, 5)
            )
