from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-ticket", views.addTicket, name="addTicket")
]