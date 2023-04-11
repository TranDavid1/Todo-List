# start selenium webdriver to create Firefox browser window
# from django.test import LiveServerTestCase

from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.by import By

class ItemValidationTest(FunctionalTest):
    def get_error_element(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.has-error')
    
    def test_cannot_add_empty_list_items(self):
        # user goes to homepage and attempts to submit empty
        # list item
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        # home page refreshes, and there is an error message saying
        # that items in list cannot be blank
        self.wait_for(lambda: 
            # use CSS class .has-error to mark error text
            # self.browser.find_elements(By.CSS_SELECTOR, '.has-error').text,
            # "You can't have an empty item in a list"
            self.browser.find_element(
                By.CSS_SELECTOR, '#id_text:invalid'
            )
        )

        # try again with text for the item
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, '#id_text:valid'
        ))
        
        # successful submission
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # try to submit a second blank item into list
        self.get_item_input_box().send_keys(Keys.ENTER)

        # browser will not allow
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, '#id_text:invalid'
        ))

        # send the same warning
        # self.wait_for(lambda: self.assertEqual(  
        #     # use CSS class .has-error to mark error text
        #     len(self.browser.find_elements(By.CSS_SELECTOR, '.has-error')),
        #     1,
        #     "You can't have an empty item in a list"
        # ))

        # correctly fill in text into item
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # go to home page and start a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy snacks')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy snacks')

        # attempt to enter a duplicate item
        self.get_item_input_box().send_keys('Buy snacks')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # send error message
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text,
            "You already have this in your list"
        ))

    def test_error_messages_are_cleared_on_input(self):
        # start a new list and cause validation error
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Banter too thick')
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            # is_displayed() tells you if element is visible or not
            self.get_error_element.is_displayed()
        ))

        # start typing into input box to clear error
        self.get_item_input_box().send_keys('a')

        # error message dissapears
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element.is_displayed()
        ))