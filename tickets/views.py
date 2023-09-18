from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "tickets/tickets.html")
 
def addTicket(request):
    return render(request, "tickets/add-ticket.html")