from django.test import TestCase
from .models import Machine, Issue

class TestViews(TestCase):
    """
    Test issue application views
    """
    def setUp(self):
        machine_a = Machine(
            name='test machine',
            slug='test-machine',
            description='Test description',
        )

        machine_a.save()
        self.machine_a = machine_a

        machine_b = Machine(
            name='test machine b',
            slug='test-machine-b',
            description='Test description b',
        )

        machine_b.save()
        self.machine_b = machine_b

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
        self.assertEqual(machine_count, 2)

    def test_issue_exists(self):
        """
        Checks issues exists
        """
        issue_count = Issue.objects.all().count()
        self.assertEqual(issue_count, 1)
    
    def test_issue_search(self):
        """
        Test issue search
        """
        issue = self.issue_a.machine.name
        issue_formatted = issue.replace(' ', '').strip()

        test_search = '  t  '
        test_search_formatted = test_search.replace(' ', '').strip()

        self.assertIn(test_search_formatted, issue_formatted)

        for item in issue_formatted:
            test_search = '  t  x '
            test_search_formatted = test_search.replace(' ', '').strip()

            if item == test_search_formatted:

                self.assertEqual(item, test_search_formatted)

            else:
                self.assertNotEqual(item, test_search_formatted)

    def test_change_status_of_machine(self):
        """
        Test changing the status of a machine
        """
        self.assertTrue(self.machine_a.status)
        
        all_machines = Machine.objects.all()

        for machine in all_machines:
            if machine.name == self.issue_a.machine.name:
                self.assertEqual(str(machine.name), self.issue_a.machine.name)
                machine.status = False
                machine.save()
                self.assertFalse(machine.status)

            else:
                self.assertNotEqual(
                    str(machine.name),
                    self.issue_a.machine.name
                    )
                machine.status = True
                machine.save()
                self.assertTrue(machine.status)

    def test_delete_issue(self):
        """
        Test delete an issue
        """
        issue = self.issue_a

        issue.delete()

        issue_count = Issue.objects.all().count()
        self.assertEqual(issue_count, 0)
