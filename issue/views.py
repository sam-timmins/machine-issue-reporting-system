from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    """
    Views the homepage
    """
    template_name = 'index.html'