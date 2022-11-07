from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """NewVisitor Test"""

    def setUp(self):
        """Set up"""
        self.browser = webdriver.Edge()
        self.base_url = "http://localhost:8000"

    def tearDown(self):
        """Tear down"""
        self.browser.quit()

    def test_start_a_list_and_receive_it_later(self):
        """Start a list and receive"""
        self.browser.get(self.base_url)
        # we see To Do title and header
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        print(header_text)
        self.assertEqual("To-Do", header_text)
        # enter the list element
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter a to-do item"
        )
        # we enter the new item "apply to a job" in the input box
        inputbox.send_keys("Apply to a job")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Apply to a job' for row in rows)
        )
        # we see the new item in the list
        self.fail("Stop test!")


if __name__ == "__main__":
    unittest.main(warnings='ignore')
