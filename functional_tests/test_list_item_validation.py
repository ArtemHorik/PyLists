from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unittest import skip


class ItemValidationTest(FunctionalTest):
    """Test list item validation"""

    def test_cannot_add_empty_list_items(self):
        """test cannot add empty list items"""
        # we open home page and try to press Enter
        self.browser.get(self.live_server_url)
        self.create_list_item("")

        # Page refreshes and we get empty list error
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, ".has-error").text,
            "You can't have an empty list item"
        ))

        # now we try it with text entered
        self.create_list_item("Buy milk")
        self.wait_for_row_in_list_table("1: Buy milk")

        # now we try to create empty list item again
        self.create_list_item("")

        # we got same empty list error
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, ".has-error").text,
            "You can't have an empty list item"
        ))

        # but we can fix it by adding some text
        self.create_list_item("Make tea")
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for_row_in_list_table("2: Make tea")
