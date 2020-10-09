from django.contrib import admin
from .models import Event, Ticket, UserProfile

# Register your models here.
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(UserProfile)