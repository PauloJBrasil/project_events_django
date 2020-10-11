from datetime import timedelta

from django.db import models

# Create your models here.
from django.utils import timezone

class Age_rating(models.Model):
    age = models.IntegerField(default=None)
    public = models.CharField(max_length=150)

    def __str__(self):
        return self.public

class Category(models.Model):
    title = models.CharField(max_length=150)
    age_rating = models.ForeignKey(Age_rating, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    pub_date = models.DateTimeField('date published')
    date = models.DateTimeField(null=False)
    limit_ticket = models.IntegerField(default=None, editable=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    
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
