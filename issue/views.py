from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views import generic
from django.urls import reverse_lazy

from .models import Machine


class Homepage(TemplateView):
    """
    Views the homepage
    """
    template_name = 'index.html'


class Dashboard(generic.ListView):
    """
    View for the machines model ordered by the status, then
    name
    """
    queryset = Machine.objects.all().order_by('status', 'name')
    template_name = 'pages/dashboard.html'


class CreateMachine(CreateView):
    """
    Views the Create Machine page with all fields available to create a
    new object using the Machine model
    """
    template_name = 'pages/create-machine.html'
    fields = '__all__'
    queryset = Machine.objects
    success_url = reverse_lazy('dashboard')