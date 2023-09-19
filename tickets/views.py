from django.shortcuts import render
from django.http import HttpResponse
from .forms import  AddTicketForm
from .models import Ticket
import datetime

def index(request):
    return render(request, "tickets/tickets.html")
 
def addTicket(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            Ticket.objects.create(
                subject = form.cleaned_data["subject"],
                description = form.cleaned_data["description"],
                requestor = request.user,
                created_at = datetime.datetime.now()
                )
            return render(request, "tickets/tickets.html")
    else:
        form = AddTicketForm()
    return render(request, "tickets/add-ticket.html", {"form": form})