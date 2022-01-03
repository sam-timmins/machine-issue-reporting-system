from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic

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