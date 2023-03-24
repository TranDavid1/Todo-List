from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

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
        # create HttpRequest object, which Django will see when user asks for page
        request = HttpRequest()
        # pass the object to home_page view
        response = home_page(request)
        # extract contents of response, .decode() converts into string of HTML
        html = response.content.decode('utf-8')
        # check to see that it starts with an <html> tag
        self.assertTrue(html.startswith('<html>'))
        # check to see if there's a <title> tag in the middle, with words "To-Do lists" in it
        self.assertIn('<title>To-Do lists</title>', html)
        # check to see that it ends with an <html> tag
        self.assertTrue(html.endswith('</html>'))
