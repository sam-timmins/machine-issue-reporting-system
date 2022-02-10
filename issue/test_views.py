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

        machine_a.save()
        self.machine_a = machine_a

        issue_a = Issue(
            machine=machine_a,
            description='Test issue description'
        )

        issue_a.save()
        self.issue_a = issue_a

    def test_machine_exists(self):
        """
        Checks the machine exists
        """
        machine_count = Machine.objects.all().count()
        self.assertEqual(machine_count, 1)
