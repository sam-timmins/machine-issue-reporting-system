from django.shortcuts import render
from django.views.generic import TemplateView


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