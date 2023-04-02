# start selenium webdriver to create Firefox browser window
# from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
from selenium.webdriver.common.by import By

# max time we're prepared to wait
MAX_WAIT = 10

class LayoutAndStylingTest(FunctionalTest):
        def test_layout_and_styling(self):
            # home page
            self.browser.get(self.live_server_url)
            self.browser.set_window_size(1024, 768)

            # input box centered
            inputbox = self.browser.find_element(By.ID, 'id_new_item')
            # assertAlmostEqual to deal with rounding errors
            self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
            )

            # second inputbox should also be centered
            inputbox.send_keys('testing')
            inputbox.send_keys(Keys.ENTER)
            self.wait_for_row_in_list_table('1: testing')
            inputbox = self.browser.find_element(By.ID, 'id_new_item')
            self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
            )

if __name__ == '__main__':
    unittest.main()

# browser.quit()
