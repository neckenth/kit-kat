from calendar import HTMLCalendar
from .models import Request

# https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, requests):
        requests_per_day = requests.filter(start_date__day=day)
        d = ''
        for request in requests_per_day:
            d += f"<li><a href='/kitkat/requests/{request.id}'>{request.title}</a></li>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, requests):
        week = ''
        for d in theweek:
            week += self.formatday(d[0], requests)
        return f'<tr>{week}</tr>'

    def formatmonth(self, withyear=True):
        requests = Request.objects.filter(
            start_date__year=self.year, start_date__month=self.month)
        cal = f"<table border='0' cellpadding='0' cellspacing='0' class='calendar'>\n"
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, requests)}\n"
        return cal
