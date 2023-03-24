from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        # resolve is function that Django uses to resolve URLs and find what view function
        # they should map to
        found = resolve('/')
        # checking that resolve, with "/", the root of the site, finds a function called home_page
        self.assertEqual(found.func, home_page)
