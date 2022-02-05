from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):
    """
    Issue form with description field that uses tyhe Issue model
    """
    class Meta:
        model = Issue
        fields = (
            'description',
        )
