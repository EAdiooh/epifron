from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update-ticket-assignee", views.update_ticket_assignee, name="updateTicketAssignee"),
    path("update-ticket-responsible", views.update_ticket_responsible, name="updateTicketResponsible"),
    path("add-ticket", views.addTicket, name="addTicket")
]