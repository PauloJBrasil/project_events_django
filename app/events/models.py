from datetime import timedelta

from django.db import models

# Create your models here.
from django.utils import timezone


class Event(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    category = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    date = models.DateTimeField(null=False)
    limit_ticket = models.IntegerField(default=0, editable=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
