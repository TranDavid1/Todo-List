# start selenium webdriver to create Firefox browser window
# from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .base import FunctionalTest
import time

class NewVisitorTest(FunctionalTest):
    # test method, run by test runner
    def test_can_start_a_list_for_one_user(self):
        # Home page
        self.browser.get(self.live_server_url)

        # Page title and header mention to-do lists
        # self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Invite to enter a to-do item immediately
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Type entry into a text box

        # send_keys is Selenium's way of typing into input elements
        inputbox.send_keys('Study for quiz')

        # Upon hitting enter, page should update, and then page should list
        # "1: " previous entry, as an item in a to-do list

        # Keys class lets us send special keys like 'Enter'
        inputbox.send_keys(Keys.ENTER)
        # time.sleep is to make sure the browser finishes loading
        # before making assertion
        self.wait_for_row_in_list_table('1: Study for quiz')

        # There should still be a text box to enter another item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Study for the final exam')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Page should update again, and should show 2 items
        self.wait_for_row_in_list_table('2: Study for the final exam')
        self.wait_for_row_in_list_table('1: Study for quiz')
        # Site should generate a unique URL, with explanatory text
        # self.fail('Finish the test!')

        # Upon visiting the URL, the to-do list with 2 items should still be there

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # start a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Study for quiz')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Study for quiz')

        # list should have a unique URL
        list_one_url = self.browser.current_url
        # assertRegex is a helper function from unittest to check whether a string matches
        # a string expression
        # use it to determine is out REST-like design has been implemented
        self.assertRegex(list_one_url, '/lists/.+')

        # new user, with new browser session
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # upon visiting home page, there should be no signs of previous list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Study for quiz', page_text)
        self.assertNotIn('Study for final exam', page_text)

        # start a new list by entering a new item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk from store')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk from store')

        # check that URL is unique
        list_two_url = self.browser.current_url
        self.assertRegex(list_two_url, '/lists/.+')
        self.assertNotEqual(list_two_url, list_one_url)

        # check for traces of list_one_url
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Study for quiz', page_text)
        self.assertIn('Buy milk from store', page_text)

if __name__ == '__main__':
    unittest.main()

# browser.quit()
