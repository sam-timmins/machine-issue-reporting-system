from .models import User

from django import forms
from django.contrib.auth.forms import UserChangeForm


class EditStaffStatusForm(UserChangeForm):

    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            'is_staff',
        )
