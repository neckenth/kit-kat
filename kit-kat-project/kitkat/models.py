import datetime as dt
import businesstime
from uuid import uuid4

from django.db import models
from django.db.models import fields
from django.conf import settings
from django.dispatch import receiver

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

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    EMP = 'EMP'
    MAN = 'MAN'
    USER_TYPE_CHOICES = [
        (EMP, 'Employee'),
        (MAN, 'Manager')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    team = models.CharField(max_length=50, choices=TEAM_CHOICES, blank=True)
    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES, default=EMP)

    def __str__(self):
        return f"{self.last_name, self.first_name}"


class Team(models.Model):
    name = models.CharField(max_length=25, choices=TEAM_CHOICES)
    manager = models.OneToOneField('Profile', on_delete=models.CASCADE, related_name='manager_of')

    def __str__(self):
        return self.name

class Request(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hours = models.IntegerField(blank=True)

    def __str__(self):
        return f"request # {self.id} by {self.user.first_name}"

    def get_hours(self):
        business_time = businesstime.BusinessTime(holidays=businesstime.holidays.usa.USFederalHolidays())
        t = business_time.businesstimedelta(self.start_date, self.end_date)
        print(t)
        hours = 0
        elapsed_time = self.end_date - self.start_date
        return elapsed_time / dt.timedelta(minutes=60)
    
    def is_in_future(self):
        return self.start_date >= dt.datetime.now()
    
    def save(self, *args, **kwargs):
        self.hours = self.get_hours()
        super(Request, self).save(*args, **kwargs)
        

