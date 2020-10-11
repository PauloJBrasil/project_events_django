from django.contrib import admin
from .models import Event, Ticket, UserProfile, Category, Age_rating

# Register your models here.
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Age_rating)