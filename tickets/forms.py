from django import forms
from django.forms import ModelForm
from .models import Ticket

class AddTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('subject', 'description')

def addTicket(request):
    form = AddTicketForm(request.POST)
    