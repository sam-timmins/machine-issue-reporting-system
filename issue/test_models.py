from django.test import TestCase

from .models import Machine, Issue


class TestModels(TestCase):
    """
    Test models
    """
    def test_machine_string_item_returns_string(self):
        """
        Test to check the machine string item returns a string
        """
        machine = Machine.objects.create(
            name='Test Machine'
        )

        self.assertEqual(str(machine), 'Test Machine')

    def test_issue_string_item_returns_string(self):
        """
        Test to check the issue string item returns a string
        """
        machine = Machine.objects.create(
            name='Test Machine'
        )

        issue = Issue.objects.create(
            machine=machine
        )

        self.assertEqual(str(issue), 'Test Machine')
