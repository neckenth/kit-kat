from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Team, Request, Profile

admin.site.unregister(User)
admin.site.register([User, Profile])
admin.site.register(Team)
admin.site.register(Request)



