from .models import Issue

from django import forms


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('description',)