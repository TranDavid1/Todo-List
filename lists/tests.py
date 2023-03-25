from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        # resolve is function that Django uses to resolve URLs and find what view function
        # they should map to
        found = resolve('/')
        # checking that resolve, with "/", the root of the site, finds a function called home_page
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # instead of creating HttpRequest object manually, we call self.client.get, and then
        # pass in the url we want to test
        response = self.client.get('/')

        # test method from Django TestCase that checks what template was used to render
        # a response
        self.assertTemplateUsed(response, 'home.html')
