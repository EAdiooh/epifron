from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  AddTicketForm, RegisterInterventionForm
from .models import Ticket, TicketIntervention, TicketStatus
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods

def index(request):
    responsibles = [];
    technicians = [];
    ticket_status = [];
    if request.user.groups.filter(name="responsible").exists():
        user_tickets = Ticket.objects.filter( (Q(assignee__isnull = True) | Q(responsible__isnull = True) ) | Q(responsible = request.user))
        responsibles = get_user_model().objects.filter(groups__name="responsible")
        technicians = get_user_model().objects.filter(groups__name="technician")
    elif request.user.groups.filter(name="technician").exists():
        user_tickets = Ticket.objects.filter(assignee = request.user)
    else:
        user_tickets = Ticket.objects.filter(requestor = request.user)
    
    context = {"user_tickets": user_tickets, "responsibles": responsibles, "technicians": technicians, "ticket_status": [c[0] for c in Ticket.status.field.choices]}
    return render(request, "tickets/tickets.html", context)

@require_http_methods(['POST'])
def update_ticket_status(request):
    ticket_id = request.POST.get("ticket_id")
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.status = request.POST.get("status")
    ticket.last_update = timezone.now()
    ticket.save()
    
    user_tickets = Ticket.objects.filter(assignee = request.user)
    responsibles = get_user_model().objects.filter(groups__name="responsible")
    technicians = get_user_model().objects.filter(groups__name="technician")

    context = {"user_tickets": user_tickets, "responsibles": responsibles, "technicians": technicians, "ticket_status": [c[0] for c in Ticket.status.field.choices]}
    return render(request, "tickets/table.html", context)

@require_http_methods(['POST'])
def update_ticket_assignee(request):
    ticket_id = request.POST.get("ticket_id")
    assignee = get_user_model().objects.get(username=request.POST.get("technician")) 
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.assignee =  assignee
    ticket.save()
    
    user_tickets = Ticket.objects.filter( (Q(assignee__isnull = True) | Q(responsible__isnull = True) ) | Q(responsible = request.user))
    responsibles = get_user_model().objects.filter(groups__name="responsible")
    technicians = get_user_model().objects.filter(groups__name="technician")
    context = {"user_tickets": user_tickets, "responsibles": responsibles, "technicians": technicians}
    return render(request, "tickets/table.html", context)

@require_http_methods(['POST'])
def update_ticket_responsible(request):
    ticket_id = request.POST.get("ticket_id")
    responsible = get_user_model().objects.get(username=request.POST.get("responsible")) 
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.responsible =  responsible
    ticket.save()

    user_tickets = Ticket.objects.filter( (Q(assignee__isnull = True) | Q(responsible__isnull = True) ) | Q(responsible = request.user))
    responsibles = get_user_model().objects.filter(groups__name="responsible")
    technicians = get_user_model().objects.filter(groups__name="technician")
    context = {"user_tickets": user_tickets, "responsibles": responsibles, "technicians": technicians}
    return render(request, "tickets/table.html", context)

 
def addTicket(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            Ticket.objects.create(
                subject = form.cleaned_data["subject"],
                description = form.cleaned_data["description"],
                requestor = request.user,
                created_at = timezone.now()
                )
            return redirect("index")
    else:
        form = AddTicketForm()
    return render(request, "tickets/add-ticket.html", {"form": form})

def registerIntervention(request, ticket_id):
    if request.method == "POST":
        form = RegisterInterventionForm(request.POST)
        if form.is_valid():
            ticket = Ticket.objects.get(pk=ticket_id)
            TicketIntervention.objects.create(
                details = form.cleaned_data["details"],
                worker = request.user,
                ticket_id = ticket,
                intervention_debut = form.cleaned_data["intervention_debut"],
                intervention_end = form.cleaned_data["intervention_end"],
                created_at = timezone.now()
                )
            ticket.last_update = timezone.now()
            ticket.save()
            return redirect("index")
    else:
        ticket = Ticket.objects.get(pk=ticket_id)
        form = RegisterInterventionForm()
        context = {"form": form, "ticket": ticket}
    return render(request, "tickets/register-intervention.html", context)

def displayIntervention(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket_interventions = TicketIntervention.objects.filter(ticket_id = ticket)
    context = {"ticket_interventions": ticket_interventions, "ticket":ticket}
    return render(request, "tickets/display-intervention.html", context)