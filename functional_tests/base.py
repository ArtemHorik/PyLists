from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

import os
import time


class FunctionalTest(StaticLiveServerTestCase):
    """Functional test"""
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
        input_box = self.get_item_input_box()
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

    def wait_for(self, fn):
        """wait"""
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_input_box(self):
        """Get item input box"""
        return self.browser.find_element(By.ID, 'id_text')

