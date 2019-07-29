from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Request

from .models import TEAM_CHOICES, USER_TYPE_CHOICES


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=200, required=True)
    team = forms.CharField(widget=forms.Select(choices=TEAM_CHOICES))
    user_type = forms.CharField(widget=forms.Select(choices=USER_TYPE_CHOICES))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username", "password1", "password2", "first_name", "last_name",
            "email", "team", "user_type"
        )


class TimeOffRequestForm(ModelForm):
    class Meta:
        model = Request
        exclude = ['hours', 'user']
