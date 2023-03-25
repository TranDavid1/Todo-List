from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        # resolve is function that Django uses to resolve URLs and find what view function
        # they should map to
        found = resolve('/')
        # checking that resolve, with "/", the root of the site, finds a function called home_page
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        # instead of creating HttpRequest object manually, we call self.client.get, and then
        # pass in the url we want to test
        response = self.client.get('/')

        # test method from Django TestCase that checks what template was used to render
        # a response
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        # check that the text from POST request is in the rendered HTML
        self.assertIn('A new list item', response.content.decode())
        # check whether we're still using the template
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_item(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Second item')
