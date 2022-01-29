from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Machine, Issue, User
from .forms import IssueForm, EditStaffStatusForm

from env import (
    UNIVERSITY_NAME,
    FACEBOOK_LINK,
    INSTAGRAM_LINK,
    TWITTER_LINK,
    MACHINE_CARDS_CURRENT_ISSUE_TEXT,
    NO_ISSUES_MODAL_TITLE,
    NO_ISSUES_TEXT
)


def delete_issue(request, pk):
    """
    Deletes the issue from the database using it's primary key
    and changes the status of the machine depending on if there are no
    longer any open issues related to it.
    """
    issue = Issue.objects.get(pk=pk)
    machine = issue.machine

    issue.delete()

    all_issues = Issue.objects.all()
    all_machines = Machine.objects.all()

    for item in all_machines:

        if item.__str__() not in list(x.__str__() for x in all_issues):
            item.status = True
            item.save()

    messages.success(request, 'Successfully deleted issue')

    return redirect('open-issues')


def delete_machine(request, pk):
    """
    Deletes the machine from the database using it's primary key
    """

    machine = Machine.objects.get(pk=pk)
    machine.delete()

    messages.success(request, 'Successfully deleted machine')

    return redirect('dashboard')


class Homepage(TemplateView):
    """
    Views the homepage
    """
    template_name = 'index.html'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }


class ViewAllUsers(generic.ListView):
    """
    Views all users
    """
    queryset = User.objects.all().order_by('-is_staff', 'last_name')
    template_name = 'pages/all-users.html'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }


class EditStaffStatus(View):
    def get(self, request, pk, *args, **kwargs):
        queryset = User.objects
        user = get_object_or_404(queryset, pk=pk)
        profile = user.pk

        return render(
            request,
            'pages/edit-staff-status.html',
            {
                'user': user,
                'profile': profile,
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = User.objects
        user = get_object_or_404(queryset, pk=pk)
        edit_staff_status_form = EditStaffStatusForm(data=request.POST)
        all_users = User.objects.all().order_by('-is_staff', 'last_name')

        if edit_staff_status_form.is_valid():

            user.is_staff = not user.is_staff
            user.save()

        else:
            edit_staff_status_form = EditStaffStatusForm()

        return render(
            request,
            'pages/all-users.html',
            {
                'all_users': all_users,
                'edit_status-form': EditStaffStatusForm()
            },
        )

    

    
class UserEditProfile(SuccessMessageMixin, UpdateView):
    """
    Views the Edit User Profile page
    using the User model
    """
    queryset = User.objects
    fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]
    template_name = 'pages/edit-profile.html'
    success_url = reverse_lazy('dashboard')
    success_message = '%(username)s successfully updated'

    def add_message(self):
        return self.success_message

    def get_object(self):
        return self.request.user

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }


class Dashboard(generic.ListView):
    """
    View for the machines model ordered by the status, then
    name
    """
    queryset = Machine.objects.all().order_by('status', 'name')
    template_name = 'pages/dashboard.html'
    paginate_by = 6

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        'current_issue_text': MACHINE_CARDS_CURRENT_ISSUE_TEXT,
        }


class SearchMachines(ListView):
    """
    Searches the machine model
    """
    model = Machine
    template_name = 'pages/dashboard.html'

    def get_queryset(self):
        query = self.request.GET.get('searchbar')
        return Machine.objects.filter(name__icontains=query)


class IssueList(generic.ListView):
    """
    View for display of the issue model ordered by newest
    to oldest entry
    """
    queryset = Issue.objects.order_by('-created_at')
    template_name = 'pages/issue-list.html'
    paginate_by = 6

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        'no_issues_modal_title': NO_ISSUES_MODAL_TITLE,
        'no_issue_text': NO_ISSUES_TEXT,
        }


class SearchIssues(ListView):
    """
    Searches the machine model
    """
    model = Issue
    template_name = 'pages/issue-list.html'

    def get_queryset(self):
        query = self.request.GET.get('searchbar-issues')

        results = Issue.objects.filter(description__icontains=query)

        if not results:
            return Issue.objects.order_by('-created_at')
        else:
            return results


class CreateMachine(SuccessMessageMixin, CreateView):
    """
    Views the Create Machine page with all fields available to create a
    new object using the Machine model
    """
    template_name = 'pages/create-machine.html'
    fields = '__all__'
    queryset = Machine.objects
    success_url = reverse_lazy('dashboard')
    success_message = '%(name)s was successfully created'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }

    def add_message(self):
        return self.success_message


class EditMachine(SuccessMessageMixin, UpdateView):
    """
    Views the Edit Machine page with 'name', 'description', 'image'
    and 'status' as available fields using the Machine model
    """
    queryset = Machine.objects
    template_name = 'pages/edit-machine.html'
    fields = ['name', 'description', 'image', 'status']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('dashboard')
    success_message = '%(name)s was successfully edited'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }

    def add_message(self):
        return self.success_message


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
        issues = machine.issues

        return render(
            request,
            'pages/machine-details.html',
            {
                'machine': machine,
                'issues': issues,
                'issue_form': IssueForm(),
                'university_name': UNIVERSITY_NAME,
                'facebook': FACEBOOK_LINK,
                'instagram': INSTAGRAM_LINK,
                'twitter': TWITTER_LINK,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Machine.objects
        machine = get_object_or_404(queryset, slug=slug)
        issues = machine.issues
        issue_form = IssueForm(data=request.POST)

        messages.success(request, 'Issue for was successfully created.')

        if issue_form.is_valid():
            issue_form.instance.user = request.user
            issue = issue_form.save(commit=False)
            issue.machine = machine
            machine.status = False
            machine.save()
            issue.save()
        else:
            issue_form = IssueForm()

        return render(
            request,
            'pages/machine-details.html',
            {
                'machine': machine,
                'issues': issues,
                'issue_form': IssueForm(),
                'university_name': UNIVERSITY_NAME,
                'facebook': FACEBOOK_LINK,
                'instagram': INSTAGRAM_LINK,
                'twitter': TWITTER_LINK,
            },
        )
