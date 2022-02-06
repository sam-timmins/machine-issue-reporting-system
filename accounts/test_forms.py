from django.test import TestCase

from accounts.forms import EditStaffStatusForm
from accounts.models import User


class TestEditStaffStatusForm(TestCase):
    """
    Testcase for the Edit Staff Status Form
    """

    def test_is_staff_field_is_in_form(self):
        """
        Test that the is_staff field is in the form
        """
        form = EditStaffStatusForm()
        self.assertIn('is_staff', form.fields)

    def test_is_staff_is_set_to_false_as_default(self):
        """
        Test to check the is_staff boolean is set to false
        as default when a user is created
        """
        user = User.objects.create_user(
            username='Test',
            password='AnExamplePa$$word',
        )

        user = User.objects.get(id=user.id)
        self.assertEqual(user.is_staff, False)

    def test_is_staff_field_changes_on_form_submission(self):
        """
        Test the is_staff boolean toggles when form is submitted
        """
        user = User.objects.create_user(
            username='Test',
            password='AnExamplePa$$word',
            is_staff=False,
        )

        self.assertEqual(user.is_staff, False)

        response = self.client.post(
            f'/user/profile/edit/staff/status/{user.id}', {
                'is_staff': True,
            })

        user = User.objects.get(id=user.id)
        self.assertEqual(user.is_staff, True)
