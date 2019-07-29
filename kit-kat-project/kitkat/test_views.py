import datetime as dt
import pytest

from django.test import TestCase
from django.urls import reverse
from .conftest import add_user

from .models import Request


class RequestViewTests(TestCase):
    @pytest.mark.only()
    def test_add_request(self):
        """
        An authenticated user should be able to successfully
        submit a valid request

        User data should be populated from the view, not the form
        """
        (user, profile) = add_user()

        url = reverse('new_request')
        self.client.force_login(user=user)

        self.client.post(url, data={
            "start_date": dt.datetime(2019, 7, 29, 9),
            "end_date": dt.datetime(2019, 8, 1, 9),
            "note": "traveling"
        })

        request = Request.objects.get(note="traveling")

        # assert request was created
        assert request is not None

        # assert user is pulled correctly from client
        assert request.user == profile
        # assert default approval status set
        assert not request.approved
        # assert computed business hours are correct
        assert request.hours == 24


# @pytest.fixture()
# def default_user():
#     return User.objects.create(username="tester", first_name="Tester", last_name="McTestFace", email="test@test.com")

# def test_index(default_user):
