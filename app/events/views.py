from django.http import HttpResponse
from django.shortcuts import render

from .models import Event

# Create your views here.
def index(request):
    events = Event.objects.all()
    output = ', '.joint([e.title for e in events])
    return HttpResponse(output)

def event(request, event_id):
    return HttpResponse(event_id)

def ticket(request, ticket_id):
    return HttpResponse(ticket_id)