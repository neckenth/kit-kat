import datetime as dt
import businesstimedelta
import holidays as pyholidays

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

# TEAM DEFINITIONS - need to be accessible to both User and Team models
ENG = 'ENG'
PROD = 'PROD'
PS = 'PS'
SALE = 'SALE'
TEAM_CHOICES = [
    (ENG, 'Engineering'),
    (PROD, 'Product'),
    (PS, 'Partner Success'),
    (SALE, 'Sales')
]

EMP = 'EMP'
MAN = 'MAN'
USER_TYPE_CHOICES = [
    (EMP, 'Employee'),
    (MAN, 'Manager')
]

User = settings.AUTH_USER_MODEL


class Profile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    team = models.CharField(max_length=50, choices=TEAM_CHOICES, blank=True)
    user_type = models.CharField(
        max_length=3, choices=USER_TYPE_CHOICES, default=EMP)

    def __str__(self):
        return f"{self.last_name, self.first_name}"


class Team(models.Model):
    name = models.CharField(max_length=25, choices=TEAM_CHOICES)
    manager = models.OneToOneField(
        'Profile', on_delete=models.CASCADE, related_name='manager_of')

    def __str__(self):
        return self.name


class Request(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hours = models.IntegerField(blank=True)
    note = models.CharField(max_length=400, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"request # {self.id} by {self.user.first_name}"

    def get_hours(self) -> int:
        workday = businesstimedelta.WorkDayRule(start_time=dt.time(
            9), end_time=dt.time(17), working_days=[0, 1, 2, 3, 4])
        ma_holidays = pyholidays.US(state="MA")
        holidays = businesstimedelta.HolidayRule(ma_holidays)
        business_hrs = businesstimedelta.Rules([workday, holidays])
        return business_hrs.difference(self.start_date, self.end_date).hours

    def is_in_future(self) -> bool:
        return self.start_date >= dt.datetime.now()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError(
                "End date for time-off request must be after start date")

    def save(self, *args, **kwargs):
        self.hours = self.get_hours()
        self.clean()
        super(Request, self).save(*args, **kwargs)
