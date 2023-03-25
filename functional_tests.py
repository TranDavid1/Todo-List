# start selenium webdriver to create Firefox browser window
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    # start browser before/after each test
    def setUp(self):
        self.browser = webdriver.Firefox()

    # stop browser before/after each test, tearDown should run even if there's an error
    # in the test itself
    def tearDown(self):
        self.browser.quit()

    # test method, run by test runner
    def test_can_start_a_list_and_retrieve_it(self):
        # Home page
        self.browser.get('http://localhost:8000')

        # Page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Invite to enter a to-do item immediately
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
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
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Study for quiz', [row.text for row in rows])

        # There should still be a text box to enter another item
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Study for the final exam')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Page should update again, and should show 2 items
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_element(By.TAG_NAME, 'tr')
        self.assertIn('1. Study for quiz', [row.text for row in rows])
        self.assertIn(
            '2: Study for the final exam',
            [row.text for row in rows]
        )

        # Site should generate a unique URL, with explanatory text
        self.fail('Finish the test!')

        # Upon visiting the URL, the to-do list with 2 items should still be there


if __name__ == '__main__':
    unittest.main()

# browser.quit()
