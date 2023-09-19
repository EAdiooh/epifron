from django.shortcuts import render
from django.http import HttpResponse
from .forms import  AddTicketForm
from .models import Ticket
import datetime

def index(request):
    user_tickets = Ticket.objects.filter(requestor = request.user)
    context = {"user_tickets": user_tickets}
    return render(request, "tickets/tickets.html", context)
 
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