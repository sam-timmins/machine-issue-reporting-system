from pathlib import Path
import os

from django.views.generic import TemplateView


# Prevent error when hidden env.py is not found
if os.path.isfile('env.py'):
    import env


UNIVERSITY_NAME = os.environ.get('UNIVERSITY_NAME')
FACEBOOK_LINK = os.environ.get('FACEBOOK_LINK')
INSTAGRAM_LINK = os.environ.get('INSTAGRAM_LINK')
FACEBOOK_LINK = os.environ.get('FACEBOOK_LINK')
TWITTER_LINK = os.environ.get('TWITTER_LINK')
MACHINE_CARDS_CURRENT_ISSUE_TEXT = os.environ.get(
    'MACHINE_CARDS_CURRENT_ISSUE_TEXT')
NO_ISSUES_MODAL_TITLE = os.environ.get('NO_ISSUES_MODAL_TITLE')
NO_ISSUES_TEXT = os.environ.get('NO_ISSUES_TEXT')


class Homepage(TemplateView):
    """
    Views the homepage
    """
    template_name = 'index.html'

    extra_context = {
        'university_name': UNIVERSITY_NAME,
        'facebook': FACEBOOK_LINK,
        'instagram': INSTAGRAM_LINK,
        'twitter': TWITTER_LINK,
        }
