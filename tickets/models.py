from django.db import models
from django.contrib.auth.models import User

class TicketStatus(models.TextChoices):
    TO_DO = 'To Do'
    In_PROGRESS = 'In Progress'
    BLOCKED = 'Blocked'
    IN_REVIEW = 'In Review'
    DONE = 'Done'

class Ticket(models.Model):
    subject = models.CharField(max_length=100)
    requestor = models.ForeignKey(User, related_name="requestor", null=False, blank = True, on_delete=models.CASCADE)
    description = models.TextField()
    responsible = models.ForeignKey(User, related_name="responsible", null=True, blank = True, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name="assignee", null=True, blank = True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    created_at = models.DateTimeField("created at")
    last_update = models.DateTimeField("last update", null=True)

