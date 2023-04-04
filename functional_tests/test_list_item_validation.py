# start selenium webdriver to create Firefox browser window
# from django.test import LiveServerTestCase

from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.by import By

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # user goes to homepage and attempts to submit empty
        # list item
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        
        # home page refreshes, and there is an error message saying
        # that items in list cannot be blank
        self.wait_for(lambda: self.assertEqual(  
            # use CSS class .has-error to mark error text
            # self.browser.find_elements(By.CSS_SELECTOR, '.has-error').text,
            len(self.browser.find_elements(By.CSS_SELECTOR, '.has-error')),
            1,
            "You can't have an empty item in a list"
        ))

        # try again with text for the item
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Buy milk')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # try to submit a second blank item into list
        # self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # send the same warning
        # self.wait_for(lambda: self.assertEqual(  
        #     # use CSS class .has-error to mark error text
        #     len(self.browser.find_elements(By.CSS_SELECTOR, '.has-error')),
        #     1,
        #     "You can't have an empty item in a list"
        # ))

        # correctly fill in text into item
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Make tea')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')