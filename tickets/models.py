from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User

class TicketStatus(models.TextChoices):
    TO_DO = 'To Do'
    In_PROGRESS = 'In Progress'
    BLOCKED = 'Blocked'
    IN_REVIEW = 'In Review'
    DONE = 'Done'

class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    requestor = models.ForeignKey(User, related_name="requestor", null=False, blank = True, on_delete=models.CASCADE)
    description = models.TextField()
    responsible = models.ForeignKey(User, related_name="responsible", null=True, blank = True, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name="assignee", null=True, blank = True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    created_at = models.DateTimeField("created at")
    last_update = models.DateTimeField("last update", null=True)

    def __str__(self):
        return self.subject

class TicketIntervention(models.Model):
    ticket_id = models.ForeignKey(Ticket, related_name="ticket_id", null=False, blank = False, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    details = models.TextField()
    intervention_debut = models.DateTimeField("intervention debut", null=False)
    intervention_end = models.DateTimeField("intervention end", null=False)
    worker = models.ForeignKey(User, related_name="worker", null=True, blank = True, on_delete=models.CASCADE)
    created_at = models.DateTimeField("created at")

    UniqueConstraint(
        name="combine_primary_key", fields=["ticket_id", "id"]
    )
    def __str__(self):
        return self.details
