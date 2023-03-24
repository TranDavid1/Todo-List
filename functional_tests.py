# start selenium webdriver to create Firefox browser window
from selenium import webdriver
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
        self.fail('Finish test!')

        # Invite to enter a to-do item immediately
        # [...rest of comments as before]


if __name__ == '__main__':
    unittest.main()

# Type entry into a text box

# Upon hitting enter, page should update, and then page should list
# "1: " previous entry, as an item in a to-do list

# There should still be a text box to enter another item

# Page should update again, and should show 2 items

# Site should generate a unique URL, with explanatory text

# Upon visiting the URL, the to-do list with 2 items should still be there

# browser.quit()
