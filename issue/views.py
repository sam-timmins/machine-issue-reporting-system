from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views import generic, View
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


class EditMachine(UpdateView):
    """
    Views the Edit Machine page with 'name', 'description', 'image'
    and 'status' as available fields using the Machine model
    """
    queryset = Machine.objects
    template_name = 'pages/edit-machine.html'
    fields = ['name', 'description', 'image', 'status']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('dashboard')


def delete_machine(request, pk):
    """
    Deletes the machine from the database using it's primary key
    """

    machine = Machine.objects.get(pk=pk)
    machine.delete()

    return redirect('dashboard')


class MachineDetail(View):
    """
    Create a view for an individual machine which
    includes the reporting an issue form. On submission of a
    vaild form, changes the status of the machine and saves to
    both Machine and issue models.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Machine.objects
        machine = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'pages/machine-details.html',
            {
                'machine': machine,
            },
        )
