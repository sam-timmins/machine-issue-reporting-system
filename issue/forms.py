from django import forms
from django.contrib.auth.forms import UserChangeForm

from .models import Issue, User


class IssueForm(forms.ModelForm):
    """
    Issue form with description field that uses tyhe Issue model
    """
    class Meta:
        model = Issue
        fields = (
            'description',
        )
