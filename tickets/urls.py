from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update-ticket-assignee", views.update_ticket_assignee, name="updateTicketAssignee"),
    path("update-ticket-responsible", views.update_ticket_responsible, name="updateTicketResponsible"),
    path("update-ticket-status", views.update_ticket_status, name="updateTicketStatus"),
    path("add-ticket", views.addTicket, name="addTicket"),
    path("<int:ticket_id>/register-intervention", views.registerIntervention, name="registerIntervention"),
    path("<int:ticket_id>/display-intervention", views.displayIntervention, name="displayIntervention"),
]