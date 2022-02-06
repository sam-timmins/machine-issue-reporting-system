from django.test import TestCase
from .models import User


class TestViews(TestCase):
    """
    Test views within the accounts application
    """

    def test_response_of_login_page_view(self):
        """
        Test successful response to login page
        """
        response = self.client.get('/login/')
        self .assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_response_of_signup_page_view(self):
        """
        Test successful response to signup page
        """
        response = self.client.get('/signup/')
        self .assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_response_of_logout_page_view(self):
        """
        Test successful response to logout page
        """
        response = self.client.get('/logout/')
        self .assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/logout.html')

    def test_response_of_all_users_page_view(self):
        """
        Test successful response to all users page
        """
        response = self.client.get('/user/profile/all-users/')
        self .assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all-users.html')

    def test_response_of_edit_staff_status_view(self):
        """
        Test successful response to edit staff status
        """
        user = User.objects.create_user(
            username='Test',
            password='AnExamplePa$$word',
        )

        response = self.client.get(
            f'/user/profile/edit/staff/status/{user.pk}'
            )

        self .assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/edit-staff-status.html')

    def test_response_of_delete_user_view(self):
        """
        Test response of delete user view
        """
        user = User.objects.create(
            username='Test',
            password='AnExamplePa$$word',
        )

        response = self.client.get(
            f'/user/profile/delete/{user.pk}'
            )

        self.assertRedirects(response, '/user/profile/all-users/')

        existing_users = User.objects.filter(pk=user.pk)
        self.assertEqual(len(existing_users), 0)

    def test_response_of_search_users_view(self):
        """
        Test response of search users view
        """
        user = User.objects.create(
            username='Test',
            password='AnExamplePa$$word',
        )

        query = 'Test'

        self.assertEqual(str(user.username), str(query))

        response = self.client.get('/user/profile/all-users/')
        self .assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all-users.html')
