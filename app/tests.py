from django.test import TestCase
from django.urls import resolve
from .views import home_page


class HomePageTest(TestCase):
    """Home page test"""
    def test_root_url_resolves_to_home_page_view(self):
        """test: root url resolves to home page view"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
