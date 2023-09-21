from django import forms
from django.forms import ModelForm
from .models import Ticket, TicketIntervention
from .widgets import DateTimePickerInput

class AddTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('subject', 'description')

def addTicket(request):
    form = AddTicketForm(request.POST)
    
class RegisterInterventionForm(ModelForm):
    class Meta:
        model = TicketIntervention
        fields = ['details', 'intervention_debut',  'intervention_end']


        widgets = {
            'intervention_debut': DateTimePickerInput(),
            'intervention_end': DateTimePickerInput()
        }

def registerIntervention(request):
    form = RegisterInterventionForm(request.POST)
    