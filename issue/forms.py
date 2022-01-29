from .models import Issue, User

from django import forms
from django.contrib.auth.forms import UserChangeForm


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = (
            'description',
        )

       
class EditStaffStatusForm(UserChangeForm):

    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            'is_staff',
        )
