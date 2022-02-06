from django import forms
from .models import User


class EditStaffStatusForm(forms.ModelForm):
    """
    Form that can edit the user's is_staff boolean status using the User model
    """
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            'is_staff',
        )
