# start selenium webdriver to create Firefox browser window
# from django.test import LiveServerTestCase

from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

# max time we're prepared to wait
MAX_WAIT = 10

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.fail("write me!")

# browser.quit()