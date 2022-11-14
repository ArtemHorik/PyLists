from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time, os
import unittest


class NewVisitorTest(StaticLiveServerTestCase):
    """NewVisitor Test"""
    MAX_WAIT = 10

    def setUp(self):
        """Set up"""
        self.browser = webdriver.Edge()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        """Tear down"""
        self.browser.quit()

    def create_list_item(self, text):
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys(text)
        input_box.send_keys(Keys.ENTER)

    def wait_for_row_in_list_table(self, row_text):
        """Check for row in list table"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        """Start a list and receive"""
        self.browser.get(self.live_server_url)
        # we see To Do title and header
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        print(header_text)
        self.assertEqual("Start a new To-Do list", header_text)
        # enter the list element
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            "Enter a to-do item"
        )
        # we enter the new item "apply to a job" in the input box
        self.create_list_item("Apply to a job")

        self.wait_for_row_in_list_table("1: Apply to a job")
        # we enter another item - "Go to lectures"
        self.create_list_item("Go to lectures")
        # now we see both elements in list
        self.wait_for_row_in_list_table("1: Apply to a job")
        self.wait_for_row_in_list_table("2: Go to lectures")

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """test: Multiple users can start lists at different urls"""
        # first user
        self.browser.get(self.live_server_url)
        self.create_list_item("Go to lectures")
        self.wait_for_row_in_list_table("1: Go to lectures")
        # we see that our list has unique url
        first_user_url = self.browser.current_url
        self.assertRegex(first_user_url, '/lists/.+')

        # second user
        self.browser.quit()
        self.browser = webdriver.Edge()

        # we don't see previous list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Go to lectures', page_text)

        # we make a new list
        self.create_list_item("Buy milk")
        self.wait_for_row_in_list_table("1: Buy milk")

        # second user gets unique url
        second_user_url = self.browser.current_url
        self.assertRegex(second_user_url, '/lists/.+')
        self.assertNotEqual(first_user_url, second_user_url)

        # nothing from first user
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Go to lectures', page_text)
        self.assertIn("Buy milk", page_text)

    def test_layout_and_styling(self):
        """test layout and styling"""
        # we open home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # input box is perfectly centered
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=30
        )

    def test_cannot_add_empty_list_items(self):
        """test cannot add empty list items"""
        self.fail("Write me!!")
