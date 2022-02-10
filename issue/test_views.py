from django.test import TestCase
from .models import Machine, Issue

class TestViews(TestCase):
    """
    Test issue application views
    """
    def setUp(self):
        machine_a = Machine(
            name='test machine',
            description='Test description',
        )

        self.machine_list = machine_list

        issue_a = Issue(
            machine=machine_a,
            description='Test issue description'
        )

        issue_a.save()
        self.issue_a = issue_a
