from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.event, name='event'),
    path('<int:ticket_id>/', views.ticket, name='ticket')
]

