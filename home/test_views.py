from django.test import TestCase


class TestViews(TestCase):
    """
    Test views within the home application
    """

    def test_response_of_home_page_view(self):
        """
        Test successful response to home page
        """
        response = self.client.get('/')
        self .assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
