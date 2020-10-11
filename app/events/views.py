from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Event, Ticket, UserProfile

# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/index.html', context)

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    return render(request, 'events/event.html', {'event': event})

def ticket(request, ticket_id):
    return HttpResponse(ticket_id)