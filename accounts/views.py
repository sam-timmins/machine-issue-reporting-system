from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, ListView, TemplateView
from django.views import generic, View
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.views import LoginView

from .models import User
from .forms import EditStaffStatusForm

from pathlib import Path
import os

# Prevent error when hidden env.py is not found
if os.path.isfile('env.py'):
    import env


UNIVERSITY_NAME = os.environ.get('UNIVERSITY_NAME')
FACEBOOK_LINK = os.environ.get('FACEBOOK_LINK')
INSTAGRAM_LINK = os.environ.get('INSTAGRAM_LINK')
FACEBOOK_LINK = os.environ.get('FACEBOOK_LINK')
TWITTER_LINK = os.environ.get('TWITTER_LINK')
MACHINE_CARDS_CURRENT_ISSUE_TEXT = os.environ.get(
    'MACHINE_CARDS_CURRENT_ISSUE_TEXT'
    )
NO_ISSUES_MODAL_TITLE = os.environ.get('NO_ISSUES_MODAL_TITLE')
NO_ISSUES_TEXT = os.environ.get('NO_ISSUES_TEXT')


class LoginViewCustom(LoginView):
    """
    Inheriting the allauth LoginView and adding the extra content
    to the view
    """
    template_name = 'account/login.html'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }


class SignUpViewCustom(TemplateView):
    """
    Inheriting the TemplateView and adding the extra content
    to the allauth signup view
    """
    template_name = 'account/signup.html'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }


class LogoutViewCustom(TemplateView):
    """
    Inheriting the TemplateView and adding the extra content
    to the allauth slogout view
    """
    template_name = 'account/logout.html'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }


class ViewAllUsers(generic.ListView):
    """
    Views all users, ordering them firstly by if they are staff
    members and then by alphabetical order of the last name
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
    """
    View for staff members to change the is_staff status of other users
    """
    def get(self, request, pk, *args, **kwargs):
        """
        Using the User model, gets the user based on their primary key and
        renders it along with the extra context variables
        """
        queryset = User.objects
        user = get_object_or_404(queryset, pk=pk)
        profile = user.pk

        return render(
            request,
            'pages/edit-staff-status.html',
            {
                'user': user,
                'profile': profile,
                'university_name': UNIVERSITY_NAME,
                'facebook': FACEBOOK_LINK,
                'instagram': INSTAGRAM_LINK,
                'twitter': TWITTER_LINK,
            },
        )

    def post(self, request, pk, *args, **kwargs):
        """
        Checks to see if the EditStaffStatusForm is valid and then
        posts any changes to the User model to the database. Renders
        it along with the extra context variables
        """
        queryset = User.objects
        user = get_object_or_404(queryset, pk=pk)
        edit_staff_status_form = EditStaffStatusForm(data=request.POST)
        all_users = User.objects.all().order_by('-is_staff', 'last_name')

        messages.success(
            request,
            f"{user.username}'s staff status was successfully changed."
            )

        if edit_staff_status_form.is_valid():

            user.is_staff = not user.is_staff
            user.save()

        else:
            edit_staff_status_form = EditStaffStatusForm()

        return redirect('all-users')


class SearchUsers(ListView):
    """
    Searches the machine model
    """
    model = User
    template_name = 'pages/all-users.html'

    def get_queryset(self):
        query = self.request.GET.get('searchbar-users')

        results = User.objects.filter(username__icontains=query)

        if not results:
            return User.objects.order_by('-username')
        else:
            return results


def delete_user_profile(request, pk):
    """
    Deletes the user profile using the User model and the user's
    primary key. Provides a success message on deletion
    """
    user_profile = User.objects.get(pk=pk)
    delete_user = User.objects.filter(username=user_profile.username)

    delete_user.delete()
    user_profile.delete()

    messages.success(request, 'User was successfully deleted.')

    return redirect('all-users')


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
