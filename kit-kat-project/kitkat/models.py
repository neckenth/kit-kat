import datetime as dt

from django.db import models
from django.db.models import fields

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

class User(models.Model):
    EMP = 'EMP'
    MAN = 'MAN'
    USER_TYPE_CHOICES = [
        (EMP, 'Employee'),
        (MAN, 'Manager')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.CharField(max_length=50, choices=TEAM_CHOICES)
    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES, default=EMP)

    def __str__(self):
        return f"{self.last_name, self.first_name}"

class Team(models.Model):
    name = models.CharField(max_length=25, choices=TEAM_CHOICES)
    manager = models.OneToOneField('User', on_delete=models.CASCADE, related_name='manager_of')

    def __str__(self):
        return self.name

class Request(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hours = models.IntegerField(blank=True)

    def __str__(self):
        return f"request # {self.id} by {self.user.first_name}"

    def get_hours(self):
        elapsed_time = self.end_date - self.start_date
        return elapsed_time / dt.timedelta(minutes=60)
    
    def is_in_future(self):
        return self.start_date >= dt.datetime.now()
    
    def save(self, *args, **kwargs):
        self.hours = self.get_hours()
        super(Request, self).save(*args, **kwargs)
        

